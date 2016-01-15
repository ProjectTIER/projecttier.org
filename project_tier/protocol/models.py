from __future__ import unicode_literals

from datetime import date

from django import forms
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailsearch import index

from wagtail.wagtailcore.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from project_tier.home.models import StandardPage

# Protocol Home Page
# --------------------------------------------------
class ProtocolHomePage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = "Protocol Langing Page"


# Components
# --------------------------------------------------
class ComponentIndexPage(Page):
    intro = RichTextField(blank=True)

    parent_page_types = ['ProtocolHomePage']

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('intro', classname="full"),
    ]

    @property
    def components(self):
        components = ComponentPage.objects.live().descendant_of(self)

        return components

class ComponentPage(Page):
    FOLDER = 'folder'
    FILE = 'file'
    COMPONENT_TYPE_CHOICES = (
        (FOLDER, "Folder"),
        (FILE, "File")
    )

    intro = RichTextField(blank=True)
    description = RichTextField(blank=True)
    type = models.CharField(max_length=255,
                            choices=COMPONENT_TYPE_CHOICES,
                            default=FOLDER)

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('intro', classname="full"),
        FieldPanel('description', classname="full"),
        FieldPanel('type', widget=forms.RadioSelect),
    ]

    search_fields = [
        index.SearchField('title', partial_match=True),
        index.SearchField('intro', partial_match=True),
        index.SearchField('description', partial_match=True),
    ]

    parent_page_types = ['ComponentIndexPage', 'ComponentPage']

    @property
    def component_index(self):
        component_index = self.get_ancestors().type(ComponentIndexPage).last()
        return ComponentIndexPage.objects.get(pk=component_index.id)


    class Meta:
        verbose_name = "Protocol Component"
