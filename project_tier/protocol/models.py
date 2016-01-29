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

from wagtail.wagtailcore.blocks import (TextBlock, PageChooserBlock, StructBlock,
    StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock)
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailsnippets.blocks import SnippetChooserBlock

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from project_tier.home.models import StandardPage

# Protocol Home Page
# --------------------------------------------------
class ProtocolHomePage(Page):
    subtitle = models.CharField(max_length=255, blank=True)
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('subtitle'),
        index.SearchField('body'),
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('subtitle', classname="full"),
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
    ]

    @property
    def children(self):
        children = self.get_children().live().in_menu().specific()

        return children

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


# Process Pages
# --------------------------------------------------

class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))

class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()

class ProtocolProcessStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title", label='Section Title')
    h3 = CharBlock(icon="title", classname="title")

    paragraph = RichTextBlock(icon="pilcrow")
    reference_page = PageChooserBlock(icon="doc-full")
    # snippet = SnippetChooserBlock()
    embed = EmbedBlock(icon="media")
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    document = DocumentChooserBlock(icon="doc-full-inverse")


class ProtocolProcessPage(Page):
    intro = RichTextField(blank=True)
    body = StreamField(ProtocolProcessStreamBlock())

    parent_page_types = ['ProtocolHomePage', 'ProtocolProcessPage']

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
        StreamFieldPanel('body'),
    ]

    @property
    def next_page(self):
        return self.get_next_sibling()

    class Meta:
        verbose_name = "Protocol Process Page"
