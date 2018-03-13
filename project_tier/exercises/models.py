from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase


class ExercisePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'exercises.ExercisePage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class ExercisePage(Page):
    cover_sheet = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
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

    listing_excerpt = models.TextField()

    tags = ClusterTaggableManager(through=ExercisePageTag, blank=True)

    parent_page_types = ['exercises.ExerciseIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('tags'),
        FieldPanel('listing_excerpt'),
        DocumentChooserPanel('cover_sheet'),
        DocumentChooserPanel('instructor_notes'),
        DocumentChooserPanel('exercise'),
        DocumentChooserPanel('sample_solution'),
    ]


class ExerciseIndexPage(Page):
    subpage_types = ['exercises.ExercisePage']

    def get_context(self, request):
        context = super().get_context(request)

        context['exercises'] = ExercisePage.objects.child_of(self).live()

        tag = request.GET.get('tag')
        if tag:
            context['exercises'] = context['exercises'].filter(tags__name=tag)

        return context
