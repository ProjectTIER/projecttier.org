from __future__ import unicode_literals
from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):
    tagline = models.CharField(max_length=255)
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('tagline', classname='full'),
        FieldPanel('intro', classname='full'),
    ]

    @property
    def children(self):
        children = self.get_children().live().in_menu().specific()
        return children

    class Meta:
        verbose_name = "homepage"
