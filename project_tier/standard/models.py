from django.db import models
from django.shortcuts import redirect
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel, StreamFieldPanel, PageChooserPanel
)
from wagtail.search.index import SearchField
from project_tier.blocks import (
    BodyBlock, LimitedStreamBlock, ContentStreamBlock
)


class StandardIndexPage(Page):
    title_suffix = models.CharField(help_text="Additional text to display after the page title e.g. '(Version 3.0)", max_length=255, blank=True)
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.', blank=True)
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)
    body = StreamField(
        LimitedStreamBlock(
            required=False  # https://github.com/wagtail/wagtail/issues/4306#issuecomment-384099847
        ),
        blank=True
    )

    @property
    def children(self):
        return self.get_children().specific().live()

    search_fields = Page.search_fields + [
        SearchField('introductory_headline')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('title_suffix'),
        FieldPanel('listing_abstract'),
        FieldPanel('introductory_headline'),
        StreamFieldPanel('body')
    ]

    parent_page_types = ['home.HomePage', 'standard.RedirectPage']


class StandardPage(Page):
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)
    overview = RichTextField(help_text='Give a general overview of what this topic is about. Limit yourself to 3 paragraphs.', blank=True)
    body = StreamField(ContentStreamBlock())
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.', blank=True)

    @property
    def parent(self):
        return self.get_parent().specific

    search_fields = Page.search_fields + [
        SearchField('introductory_headline'),
        SearchField('overview'),
        SearchField('listing_abstract'),
        SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('listing_abstract'),
        FieldPanel('introductory_headline'),
        FieldPanel('overview'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = [
        'home.HomePage',
        'standard.StandardPage',
        'standard.StandardIndexPage',
        'standard.SectionPage'
    ]

    subpage_types = [
        'standard.StandardPage',
        'standard.SectionPage'
    ]


class SectionPage(Page):
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)
    overview = RichTextField(help_text='Give a general overview of what this topic is about. Limit yourself to 3 paragraphs.', blank=True)
    body = StreamField(BodyBlock())
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.', blank=True)

    @property
    def parent(self):
        return self.get_parent().specific

    search_fields = Page.search_fields + [
        SearchField('introductory_headline'),
        SearchField('overview'),
        SearchField('listing_abstract'),
        SearchField('body')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('listing_abstract'),
        FieldPanel('introductory_headline'),
        FieldPanel('overview'),
        StreamFieldPanel('body'),
    ]

    parent_page_types = [
        'home.HomePage',
        'standard.StandardPage',
        'standard.StandardIndexPage',
        'standard.SectionPage'
    ]

    subpage_types = [
        'standard.StandardPage',
        'standard.SectionPage',
        'exercises.ExerciseIndexPage'
    ]

    class Meta:
        verbose_name = "Standard page with content sections"


class RedirectPage(Page):
    """Dummy page with overridden URL."""

    related_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose the page to redirect to.'
    )

    def serve(self, request):
        """Redirect to the related page."""
        return redirect(self.related_page.get_url(), permanent=True)

    def get_url_parts(self, request=None):
        """Return the URL of the related page."""
        return self.related_page.get_url_parts(request)

    content_panels = Page.content_panels + [
        PageChooserPanel('related_page'),
    ]
