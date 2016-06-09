from __future__ import unicode_literals
from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase


class PersonPageTag(TaggedItemBase):
    content_object = ParentalKey('PersonPage', related_name='tagged_items')


class PersonPage(Page):
    location = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    job_titles = RichTextField(blank=True)
    intro = RichTextField(blank=True)
    biography = RichTextField(blank=True)
    website = models.URLField(max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    parent_page_types = ['PersonIndexPage']

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('biography'),
        index.SearchField('location'),
        index.SearchField('phone'),
        index.SearchField('email'),
        index.SearchField('job_titles'),
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        MultiFieldPanel(
            [
                FieldPanel('location'),
                FieldPanel('phone'),
                FieldPanel('email'),
                FieldPanel('website'),
            ],
            heading="Contact Information",
            classname="collapsible collapsed"
        ),
        FieldPanel('job_titles', classname="full"),
        FieldPanel('intro', classname="full"),
        FieldPanel('biography', classname="full"),
        ImageChooserPanel('image'),
    ]

    @property
    def person_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(PersonIndexPage).last()

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class PersonIndexPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    parent_page_types = [
        'home.HomePage',
        'standard.StandardPage',
        'PersonIndexPage'
    ]

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
    ]

    @property
    def main_groups(self):
        return self.get_children().live().in_menu()

    @property
    def secondary_groups(self):
        return self.get_children().live().not_in_menu().not_type(PersonPage)

    @property
    def people(self):
        people = PersonPage.objects.live().child_of(self).order_by('title')

        return people

    class Meta:
        verbose_name = 'Person List Page'
