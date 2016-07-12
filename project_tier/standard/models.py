from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailsearch.index import SearchField

from project_tier.blocks import BodyBlock, ContentStreamBlock


class StandardIndexPage(Page):
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.', blank=True)
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)
    body = StreamField(ContentStreamBlock(), blank=True)

    @property
    def children(self):
        return self.get_children().specific().live()

    search_fields = Page.search_fields + [
        SearchField('introductory_headline')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('listing_abstract'),
        FieldPanel('introductory_headline'),
        StreamFieldPanel('body')
    ]

    parent_page_types = ['home.HomePage']


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
        'standard.SectionPage'
    ]
