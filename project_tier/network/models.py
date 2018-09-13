from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.search import index
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
)
import datetime


class Person(models.Model):
    """
    A member of the Tier Network, including Fellows and other connections.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = models.SlugField()
    main_job_title = models.CharField(max_length=255, blank=True)
    academic_title = models.CharField(max_length=255, blank=True)
    affiliation = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    website = models.URLField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True)
    image_credit = models.CharField(max_length=255, blank=True, help_text="Add credit for photo if necessary. Note: add only their name 'Photo courtesy of' is hardcoded")

    show_in_network = models.BooleanField(default=True, blank=False)
    show_in_people = models.BooleanField(default=False, blank=False)

    CATEGORIES = (
        ('fellows', 'Fellow'),
        ('advisory_board', 'Advisory Board'),
        ('project_directors', 'Project Director'),
        ('network_other', 'Network Other')
    )
    category = models.CharField(
        max_length=255,
        choices=CATEGORIES,
        default='network_other',
        blank=False,
    )

    YEAR_CHOICES = []
    for r in range(2010, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append(
            (r, "{}–{}".format(r, r + 1))
        )

    fellowship_year = models.IntegerField(
        choices=YEAR_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class PersonIndexPage2(Page):
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.')
    body = RichTextField(blank=True)

    @property
    def fellowship_years(self):
        fellowship_years = {}
        fellows = Person.objects.filter(category='fellows', show_in_people=True)
        for fellow in fellows:
            year = fellow.fellowship_year
            try:
                fellowship_years[year]
            except KeyError:
                fellowship_years[year] = []
            fellowship_years[year].append(fellow)
        return sorted(fellowship_years.items(), reverse=True)

    parent_page_types = [
        'home.HomePage',
        'standard.StandardIndexPage',
    ]

    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('introductory_headline'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('introductory_headline'),
        FieldPanel('listing_abstract'),
        FieldPanel('body'),
    ]

    @property
    def people(self):
        people = Person.objects.filter(show_in_people=True)
        return people

    @property
    def sections(self):
        sections = []
        categories = Person.CATEGORIES
        for category in categories:
            # Get people for category
            people = self.people.filter(category=category[0])
            if people:
                sections.append({
                    "category": category,
                    "people": people
                })
        return sections

    class Meta:
        verbose_name = 'Person List Page'


class NetworkIndexPage(Page):
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.')
    body = RichTextField(blank=True)

    parent_page_types = [
        'home.HomePage',
        'standard.StandardIndexPage',
    ]

    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('introductory_headline'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('introductory_headline'),
        FieldPanel('listing_abstract'),
        FieldPanel('body'),
    ]

    @property
    def people(self):
        people = Person.objects.filter(show_in_network=True).order_by('last_name')
        return people

    class Meta:
        verbose_name = 'Network List Page'
