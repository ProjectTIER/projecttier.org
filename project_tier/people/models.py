from __future__ import unicode_literals
from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, InlinePanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from modelcluster.fields import ParentalKey
from wagtail.wagtailsnippets.models import register_snippet


@register_snippet
class PersonCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):              # __unicode__ on Python 2
        # We're returning the string that populates the snippets screen. Note it returns as plain-text
        return self.title


class PersonPage(Page):
    location = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    main_job_title = models.TextField(blank=True)
    academic_title = models.TextField(blank=True)
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)
    biography = RichTextField(blank=True)
    website = models.URLField(max_length=255, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    fellowship_year = models.TextField(blank=True)

    @property
    def categories(self):
        categories = [
            n.category for n in self.person_category_relationship.all()
        ]
        return categories

    parent_page_types = ['PersonIndexPage']

    search_fields = Page.search_fields + (
        index.SearchField('introductory_headline'),
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
        FieldPanel('main_job_title', classname="full"),
        FieldPanel('academic_title', classname="full"),
        FieldPanel('introductory_headline', classname="full"),
        FieldPanel('biography', classname="full"),
        ImageChooserPanel('image'),
        InlinePanel('person_category_relationship', label="Categories"),
        FieldPanel('fellowship_year')
    ]

    @property
    def person_index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(PersonIndexPage).last()

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class PersonIndexPage(Page):
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.')
    body = RichTextField(blank=True)
    parent_page_types = [
        'home.HomePage',
        'standard.StandardIndexPage',
        'PersonIndexPage'
    ]

    subpage_types = ['PersonPage']

    search_fields = Page.search_fields + (
        index.SearchField('introductory_headline'),
        index.SearchField('body'),
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('introductory_headline', classname="full"),
        FieldPanel('listing_abstract'),
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


class PersonCategoryRelationship(models.Model):
    person = ParentalKey(
        'PersonPage', related_name='person_category_relationship')
    category = models.ForeignKey('PersonCategory', related_name='+')

    panels = [FieldPanel('category')]
