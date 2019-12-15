from __future__ import unicode_literals
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel, PageChooserPanel, MultiFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    headline = models.CharField(max_length=255, help_text='Write a short introductory sentence about Project TIER.')
    featured_index_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose the most important index page on the site. It will be prominently featured on the home page.'
    )
    featured_index_page_2 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose an important secondary page to feature.',
        verbose_name='Secondary featured page'
    )
    featured_index_page_3 = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Choose an important secondary page to feature.',
        verbose_name='Secondary featured page'
    )
    featured_events_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Select the main events listing page.'
    )
    promo_headline = models.CharField(max_length=255, blank=True)
    promo_text = RichTextField(blank=True)
    promo_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    promo_cta_link = models.URLField(blank=True)
    promo_cta_text = models.CharField(max_length=20, blank=True)

    big_cta_show = models.BooleanField(
        default=True, verbose_name="Show big CTA?")
    big_cta_text = models.CharField(
        max_length=200, blank=True, verbose_name="Big CTA text")
    big_cta_link = models.URLField(blank=True, verbose_name="Big CTA link")

    content_panels = Page.content_panels + [
        FieldPanel('headline'),
        PageChooserPanel('featured_index_page', 'standard.StandardIndexPage'),
        MultiFieldPanel([
            PageChooserPanel('featured_index_page_2', 'standard.StandardIndexPage'),
            PageChooserPanel('featured_index_page_3', 'standard.StandardIndexPage'),
            PageChooserPanel('featured_events_page', 'events.EventIndexPage'),
        ], heading="Secondary featured section"),
        MultiFieldPanel([
            FieldPanel('promo_headline'),
            FieldPanel('promo_text'),
            ImageChooserPanel('promo_image'),
            FieldPanel('promo_cta_link'),
            FieldPanel('promo_cta_text'),
        ], heading="Promo"),
        MultiFieldPanel([
            FieldPanel('big_cta_show'),
            FieldPanel('big_cta_text'),
            FieldPanel('big_cta_link'),
        ], heading="Big CTA"),
    ]

    # Only let the root page be a parent
    parent_page_types = ['wagtailcore.Page']

    @property
    def children(self):
        children = self.get_children().live().in_menu().specific()
        return children

    class Meta:
        verbose_name = "homepage"
