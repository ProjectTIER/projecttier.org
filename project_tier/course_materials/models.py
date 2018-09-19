from django.db import models
from django.db.models import Count
from django.db.models.functions import Lower
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase

"""
The way these tags work is weird, but unavoidable? See the comment in
`project_tier.exercises.models` for more information.

TODO: Find a way to consolidate the code from both apps and clean it up.
"""

class DisciplineTag(TaggedItemBase):
    content_object = ParentalKey(
        'course_materials.CourseMaterialsPage',
        # django-modelcluster requires this to be set
        related_name='discipline_tags_relationship',
        on_delete=models.CASCADE
    )


class CourseLevelTag(TaggedItemBase):
    content_object = ParentalKey(
        'course_materials.CourseMaterialsPage',
        # django-modelcluster requires this to be set
        related_name='course_level_tags_relationship',
        on_delete=models.CASCADE
    )


class ProtocolTag(TaggedItemBase):
    content_object = ParentalKey(
        'course_materials.CourseMaterialsPage',
        # django-modelcluster requires this to be set
        related_name='protocol_tags_relationship',
        on_delete=models.CASCADE
    )


class CourseMaterialsPage(Page):
    syllabus = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    university = models.CharField(
        max_length=255,
        help_text="Name of the university this exercise originated from, ex "
                  "Harvard University"
    )
    instructor = models.CharField(
        max_length=255,
        help_text="Name of the instructor who teaches this course, ex "
                  "Janet Black"
    )
    course_name = models.CharField(
        max_length=255,
        help_text="The name of the course this exercise appears in, ex. "
                  "Statistical and Data Sciences 220"
    )
    semester = models.CharField(
        max_length=255,
        help_text="The semester of this course, ex. Spring 2017"
    )
    course_description = RichTextField(
        help_text="1-3 paragraph description of this entry."
    )
    discipline_tags = ClusterTaggableManager(
        through=DisciplineTag,
        # disabling reverse accessors solves a naming clash
        related_name="+",
        blank=True,
        verbose_name="discipline tags"
    )
    course_level_tags = ClusterTaggableManager(
        through=CourseLevelTag,
        # disabling reverse accessors solves a naming clash
        related_name="+",
        blank=True,
        verbose_name="course level tags"
    )
    protocol_tags = ClusterTaggableManager(
        through=ProtocolTag,
        # disabling reverse accessors solves a naming clash
        related_name="+",
        blank=True,
        verbose_name="protocol tags"
    )

    parent_page_types = ['course_materials.CourseMaterialsIndexPage']
    subpage_types = []

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('title'),
                FieldPanel('university'),
                FieldPanel('instructor'),
                FieldPanel('course_name'),
                FieldPanel('semester'),
                FieldPanel('course_description'),
            ],
            heading="course info",
        ),
        MultiFieldPanel(
            [
                FieldPanel('discipline_tags'),
                FieldPanel('course_level_tags'),
                FieldPanel('protocol_tags'),
            ],
            heading="tags",
        ),
        MultiFieldPanel(
            [
                DocumentChooserPanel('syllabus'),
            ],
            heading="materials",
        ),
    ]


class CourseMaterialsIndexPage(Page):
    intro = RichTextField(
        blank=True,
        help_text="1-3 paragraphs explaining the course materials."
    )

    subpage_types = ['course_materials.CourseMaterialsPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context['course_materials'] = CourseMaterialsPage.objects.child_of(self).live()

        # Filters tags by type (using reverse accessors).
        # eg. `Tag.course_materials_disciplinetag_items` will contain rows if
        # the tag is used as a DisciplineTag anywhere. Therefore, we check that
        # it's not null.
        context['discipline_tags'] = Tag.objects.filter(
            course_materials_disciplinetag_items__isnull=False
        ).annotate(
            num_results=Count('course_materials_disciplinetag_items')
        ).order_by('-num_results', Lower('name')).distinct()

        context['course_level_tags'] = Tag.objects.filter(
            course_materials_courseleveltag_items__isnull=False
        ).annotate(
            num_results=Count('course_materials_courseleveltag_items')
        ).order_by('-num_results', Lower('name')).distinct()

        context['protocol_tags'] = Tag.objects.filter(
            course_materials_protocoltag_items__isnull=False
        ).annotate(
            num_results=Count('course_materials_protocoltag_items')
        ).order_by('-num_results', Lower('name')).distinct()

        # Filters course materials by the tag name in the URL
        tag_groups = [
            # (The name in the URL, the name of the Python model attribute)
            ('disciplines', 'discipline'),
            ('course-levels', 'course_level'),
            ('protocols', 'protocol')
        ]
        # Loop through the given tag groups from above
        for tag_group in tag_groups:
            # Get URL query for this tag group
            url_query = request.GET.get(tag_group[0])

            # If the tag group isn't in this URL, move on to the next one
            if not url_query:
                continue

            # The tags in this URL for the given tag group
            tag_list = url_query.split('|')

            # Render checked tags
            context[tag_group[1] + '_tags_checked'] = tag_list

            # Filter the course materials based on the tags in the URL
            lookups = { '{}_tags__name__in'.format(tag_group[1]): tag_list }
            context['course_materials'] = context['course_materials'].filter(**lookups).distinct()

        # Info about page results
        course_materials_count = context['course_materials'].count()
        hidden_course_materials = CourseMaterialsPage.objects.count() - course_materials_count
        total_course_materials = CourseMaterialsPage.objects.count()
        context['results'] = {
            'shown': course_materials_count,
            'hidden': hidden_course_materials,
            'filtered': hidden_course_materials > 0,
            'total': total_course_materials
        }

        return context
