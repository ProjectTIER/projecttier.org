from unidecode import unidecode
from django import forms
from django.utils import timezone
from django.db import models
from django.db.models import F
from modelcluster.fields import ParentalManyToManyField
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.search import index
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel
)
import datetime
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


class Person(models.Model):
    """
    A member of the Tier Network, including Fellows and other connections.
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    slug = models.SlugField(
        help_text="All lowercase, hyphenated name that will appear in the URL."
                  " For example, entering norm-medeiros will result in the URL"
                  " projecttier.org/person/norm-medeiros"
    )
    main_job_title = models.CharField(max_length=255, blank=True)
    secondary_job_title = models.CharField(max_length=255, blank=True)
    tier_title = models.CharField(max_length=255, blank=True)
    affiliation = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    website = models.URLField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True, help_text="Note: Do not include @")
    bio = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_credit = models.CharField(max_length=255, blank=True, help_text="Add credit for photo if necessary. Note: add only their name 'Photo courtesy of' is hardcoded")

    show_in_network = models.BooleanField(default=True, blank=False)
    show_in_people = models.BooleanField(default=False, blank=False)

    joined_on = models.DateField(blank=True, null=True,
        help_text="Date this member joined the TIER network. Not publicly "
                  "visible - used to calculate NEW tags.")

    categories = models.ManyToManyField('network.PersonCategory', blank=True)

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

    def is_new(self):
        """ The person became a member within the past 30 days. """
        today = timezone.now().date()
        joined = self.joined_on
        return joined and (today - joined).days <= 30

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel('first_name'),
                FieldPanel('last_name'),
                FieldPanel('affiliation'),
                FieldPanel('main_job_title'),
                FieldPanel('secondary_job_title'),
                FieldPanel('tier_title'),
                FieldPanel('slug'),
            ],
            heading="Basic Person Info"
        ),
        MultiFieldPanel(
            [
                FieldPanel('email'),
                FieldPanel('phone'),
                FieldPanel('website'),
                FieldPanel('twitter'),
            ],
            heading="Person Contact Info"
        ),
        FieldPanel('bio'),
        MultiFieldPanel(
            [
                ImageChooserPanel('image'),
                FieldPanel('image_credit'),
            ],
            heading="Person image"
        ),
        MultiFieldPanel(
            [
                FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
                FieldPanel('show_in_network'),
                FieldPanel('show_in_people'),
                FieldPanel('fellowship_year'),
                FieldPanel('joined_on'),
            ],
            heading="Display Settings"
        ),
    ]

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


class PersonListPage(Page):
    introductory_headline = models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.')
    body = RichTextField(blank=True)

    @property
    def fellowship_years(self):
        fellowship_years = {}
        fellows = Person.objects.filter(categories__slug='fellow', show_in_people=True).order_by('last_name')
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
        people = Person.objects.filter(show_in_people=True).order_by('last_name')
        return people

    @property
    def sections(self):
        sections = []
        categories = PersonCategory.objects.all()
        for category in categories:

            if category.slug == 'network_other':
                continue

            # Get people for category
            people = self.people.filter(categories__slug=category.slug)
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

    def get_context(self, request):
        context = super().get_context(request)
        # displays the "Join the TIER Nework" block in the personlist
        # for this page.
        context['join_block'] = "true"

        return context

    @property
    def people(self):
        people = Person.objects.filter(show_in_network=True)
        # Put new people at the top. Convert is_new to a string that can be ordered.
        return sorted(people, key = lambda p: ('A' if p.is_new() else 'Z', unidecode(p.last_name).lower()))

    class Meta:
        verbose_name = 'Network List Page'


@register_snippet
class PersonCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    tier_title = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(
        null=True, blank=True,
        help_text="Lower numbers are shown first. If left blank, it will "
                  "show up at the end."
    )

    def __str__(self):              # __unicode__ on Python 2
        # We're returning the string that populates the snippets screen. Note it returns as plain-text
        return self.title

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'People category'
        verbose_name_plural = 'People categories'
