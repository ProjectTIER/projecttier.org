from __future__ import unicode_literals
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel, PageChooserPanel, MultiFieldPanel, StreamFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel

from project_tier.blocks import HomeStreamBlock


class HomePage(Page):
    headline = models.CharField(max_length=255, help_text='Write a short introductory sentence about Project TIER.')
    banner = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    body = StreamField(HomeStreamBlock())

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        ImageChooserPanel('banner'),
        StreamFieldPanel('body'),
    ]

    # Only let the root page be a parent
    parent_page_types = ['wagtailcore.Page']

    @property
    def children(self):
        children = self.get_children().live().in_menu().specific()
        return children

    class Meta:
        verbose_name = "homepage"
