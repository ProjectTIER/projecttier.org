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


# Events
# --------------------------------------------------
@register_snippet
class Component(models.Model):
    FOLDER = 'folder'
    FILE = 'file'
    COMPONENT_TYPE_CHOICES = (
        (FOLDER, "Folder"),
        (FILE, "File")
    )

    name = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    type = models.CharField(max_length=255,
                            choices=COMPONENT_TYPE_CHOICES,
                            default=FOLDER)

    panels = [
        FieldPanel('name'),
        FieldPanel('description', classname="full"),
        FieldPanel('type', classname="full", widget=forms.RadioSelect),
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
        index.SearchField('description', partial_match=True),
    ]

    def __unicode__(self):
        return self.name


class ComponentPage(Page):
    component = models.ForeignKey(
        'Component',
        null=True,
        # blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('component'),
    )

    content_panels = Page.content_panels + [
        SnippetChooserPanel('component'),
    ]

class ComponentIndexPage(Page):
    @property
    def components(self):
        components = ComponentPage.objects.live().descendant_of(self)

        return components
