from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase

"""
Okay, the way these tags work is horrifying. The below three models aren't
actual `Tag` subclasses, they're through-models. Eg, they represent the
relationship between the page and each type of tag, so don't let their names
fool you.

The Wagtail docs say to do it this way:
http://docs.wagtail.io/en/v2.0/getting_started/tutorial.html#tagging-posts

Unfortunately it doesn't cover how to have multiple tags on a single page,
which we need since we're tagging 3 different things. By default, the tags'
reverse-accessors clash. See: https://github.com/alex/django-taggit/issues/50

Per this test, we can set the `related_name` of the managers:
https://github.com/alex/django-taggit/blob/590918f/tests/models.py#L23-L25
Setting to `+` removes the reverse accessor clash.

However, since we use ParentalKey in the through-models, we're forced to set
a `related_name` for each relationship. The name cannot be the same as
the managers we add to the model, so `_relationship` has been appended to them.

It's messy, but perhaps the best way to achieve what we want here, short of
changing the actual tagging API within Wagtail or django-taggit.
"""

class DisciplineTag(TaggedItemBase):
    content_object = ParentalKey(
        'exercises.ExercisePage',
        # django-modelcluster requires this to be set
        related_name='discipline_tags_relationship',
        on_delete=models.CASCADE
    )


class CourseLevelTag(TaggedItemBase):
    content_object = ParentalKey(
        'exercises.ExercisePage',
        # django-modelcluster requires this to be set
        related_name='course_level_tags_relationship',
        on_delete=models.CASCADE
    )


class ProtocolTag(TaggedItemBase):
    content_object = ParentalKey(
        'exercises.ExercisePage',
        # django-modelcluster requires this to be set
        related_name='protocol_tags_relationship',
        on_delete=models.CASCADE
    )


class ExercisePage(Page):
    cover_sheet = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,  # cover sheet is required
        on_delete=models.SET_NULL,
        related_name='+'
    )
    instructor_notes = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    exercise = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    sample_solution = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    all_files = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="An archive containing all of this exercise's files."
    )

    listing_excerpt = models.TextField()

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

    parent_page_types = ['exercises.ExerciseIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('listing_excerpt'),
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
                DocumentChooserPanel('cover_sheet'),
                DocumentChooserPanel('instructor_notes'),
                DocumentChooserPanel('exercise'),
                DocumentChooserPanel('sample_solution'),
                DocumentChooserPanel('all_files'),
            ],
            heading="files",
        ),
    ]


class ExerciseIndexPage(Page):
    subpage_types = ['exercises.ExercisePage']

    def get_context(self, request):
        context = super().get_context(request)

        context['exercises'] = ExercisePage.objects.child_of(self).live()

        # Filters tags by type (using reverse accessors).
        # eg. `Tag.exercises_disciplinetag_items` will contain rows if
        # the tag is used as a DisciplineTag anywhere. Therefore, we check that
        # it's not null.
        context['discipline_tags'] = Tag.objects.filter(
            exercises_disciplinetag_items__isnull=False).distinct()
        context['course_level_tags'] = Tag.objects.filter(
            exercises_courseleveltag_items__isnull=False).distinct()
        context['protocol_tags'] = Tag.objects.filter(
            exercises_protocoltag_items__isnull=False).distinct()

        # Filters exercises by the tag name in the URL
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

            # Filter the exercises based on the tags in the URL
            lookups = { '{}_tags__name__in'.format(tag_group[1]): tag_list }
            context['exercises'] = context['exercises'].filter(**lookups).distinct()

        # Info about page results
        exercises_count = context['exercises'].count()
        hidden_exercises = ExercisePage.objects.count() - exercises_count
        context['results'] = {
            'shown': exercises_count,
            'hidden': hidden_exercises,
            'filtered': hidden_exercises > 0
        }

        return context
