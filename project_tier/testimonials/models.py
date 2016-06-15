from __future__ import unicode_literals
from django.db import models
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, InlinePanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from modelcluster.fields import ParentalKey
from wagtail.wagtailsnippets.models import register_snippet


class Testimonial(Orderable):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    testimony = RichTextField()

    index_page = ParentalKey('TestimonialIndexPage', related_name='related_testimonials')
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
