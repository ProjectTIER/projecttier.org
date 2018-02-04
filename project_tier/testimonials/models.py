from __future__ import unicode_literals
from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, InlinePanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.snippets.models import register_snippet


class Testimonial(Orderable):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    testimony = RichTextField()

    index_page = ParentalKey(
        'TestimonialIndexPage',
        related_name='related_testimonials',
        on_delete=models.CASCADE
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('year'),
        FieldPanel('school'),
        FieldPanel('testimony')
    ]


class TestimonialIndexPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel('related_testimonials', label='Testimonials')
    ]
