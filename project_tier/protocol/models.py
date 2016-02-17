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


# Recursively search for a protocol page's root protocol
def getProtocolParent(page):
    parent = page.get_ancestors().last()

    if not parent:
        return False

    if parent.content_type.model != 'protocolhomepage':
        return getProtocolParent(parent)

    return parent


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

    @property
    def protocol_parent(self):
        return getProtocolParent(self)


class ComponentPage(Page):
    FOLDER = 'folder'
    FILE = 'file'
    DATA = 'data'
    MULTIPLE_FILES = 'multiple'
    COMPONENT_TYPE_CHOICES = (
        (FOLDER, "Folder"),
        (FILE, "Text"),
        (DATA, "Data"),
        (MULTIPLE_FILES, "Multiple")
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

    @property
    def protocol_parent(self):
        return getProtocolParent(self)

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

class TipBlock(StructBlock):
    title = CharBlock(label='Tip Heading')
    details = RichTextBlock()

    class Meta:
        template = 'blocks/tip.html'
        icon = 'help'

class ExtendedInfoBlock(StructBlock):
    heading = CharBlock(label='Heading', help_text='The heading of an extended info setting')
    details = RichTextBlock()

    class Meta:
        template = 'blocks/extended_info.html'
        icon = 'plus-inverse'

class ProtocolProcessStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title", label='Section Title')

    paragraph = RichTextBlock(icon="pilcrow")
    rich_text = RichTextBlock(icon="pilcrow")
    embed = EmbedBlock(icon="media")
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    tip = TipBlock(label="Tip", icon="help")
    extended_info = ExtendedInfoBlock(label="Extended Info", icon="plus-inverse")
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
        next = self.get_next_sibling()
        if next:
            if next.content_type.model != 'protocolprocesspage':
                next = self.get_children().first()
            return next
        return False

    @property
    def protocol_parent(self):
        return getProtocolParent(self)

    class Meta:
        verbose_name = "Protocol Process Page"
