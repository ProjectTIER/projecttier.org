from __future__ import unicode_literals

from datetime import date, datetime

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django import forms

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailsearch import index

from wagtail.wagtailcore.blocks import TextBlock, StructBlock, StreamBlock, FieldBlock, CharBlock, RichTextBlock, RawHTMLBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock

from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

from project_tier.protocol.models import ProtocolProcessStreamBlock

# Abstract Classes
# --------------------------------------------------
# A couple of abstract classes that contain commonly used fields

class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True

# Common Page Components
# --------------------------------------------------

class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True

# Home Page
# --------------------------------------------------

class PullQuoteBlock(StructBlock):
    quote = TextBlock("quote title")
    attribution = CharBlock()

    class Meta:
        icon = "openquote"


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', 'Wrap left'), ('right', 'Wrap right'), ('mid', 'Mid width'), ('full', 'Full width'),
    ))


class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', 'Normal'), ('full', 'Full width'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()


class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"


class StandardStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow")
    paragraph = RichTextBlock(icon="pilcrow")
    aligned_image = ImageBlock(label="Aligned image", icon="image")
    pullquote = PullQuoteBlock()
    aligned_html = AlignedHTMLBlock(icon="code", label='Raw HTML')
    document = DocumentChooserBlock(icon="doc-full-inverse")


class HomePage(Page):
    tagline = models.CharField(max_length=255)
    intro = RichTextField(blank=True)

    parent_page_types = []

    content_panels = Page.content_panels + [
        FieldPanel('tagline', classname="full"),
        FieldPanel('intro', classname="full"),
    ]

    @property
    def children(self):
        children = self.get_children().live().in_menu().specific()

        return children

    @property
    def news(self):
        news = NewsArticle.objects.live()
        news = news.filter(expire_at__gte=datetime.now())
        news = news.order_by('go_live_at')
        return news

    class Meta:
        verbose_name = "Homepage"


# Standard Page
# --------------------------------------------------

# class StandardPageRelatedLink(Orderable, RelatedLink):
#     page = ParentalKey('StandardPage', related_name='related_links')
#
class StandardPage(Page):
    intro = RichTextField(blank=True)
    body = StreamField(ProtocolProcessStreamBlock())

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('intro', classname="full"),
        StreamFieldPanel('body'),
        # InlinePanel('related_links', label="Related links"),
    ]

    # parent_page_types = [HomePage, 'StandardPage']

    class Meta:
        verbose_name = "Page"

class TestPage(Page):
    template_path = models.CharField(max_length=255, blank=True, help_text='Use any filename in home/template/home/')

    def get_template(self, request):
        if self.template_path:
            return "home/%s" % (self.template_path)

        return 'home/standard_page.html'

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('template_path', classname="full"),
    ]

    class Meta:
        verbose_name = "Test Page"


# Landing Page
# --------------------------------------------------
class LandingPage(Page):
    parent_page_types = ['Homepage', 'StandardPage']
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
    ]

    @property
    def children(self):
        children = Page.objects.live().descendant_of(self)

        return children

# Events
# --------------------------------------------------
class EventIndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('EventIndexPage', related_name='related_links')

class EventIndexPage(Page):
    UPCOMING = 'gte'
    PAST = 'lt'
    EVENT_LIST_CHOICES = (
        (UPCOMING, 'Upcoming Events'),
        (PAST, 'Past Events'),
    )
    show_events = models.CharField(max_length=3,
                                  choices=EVENT_LIST_CHOICES,
                                  default=UPCOMING)

    intro = RichTextField(blank=True)

    parent_page_types = ['Homepage', 'StandardPage']

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    content_panels = [
        FieldPanel('title', classname="title"),
        FieldPanel('intro', classname="full"),
        FieldPanel('show_events', classname=""),
        InlinePanel('related_links', label="Related links"),
    ]

    @property
    def events(self):
        events = EventPage.objects.live()

        kwargs = {
            '{0}__{1}'.format('date_from', self.show_events): date.today(),
        }

        events = events.filter(**kwargs)

        events = events.order_by('date_from' if self.show_events == 'gte' else '-date_from')

        return events

    @property
    def past_events(self):
        events = EventPage.objects.live().filter(date_from__lt=date.today())
        events = events.order_by('-date_from')
        events = events.all()[:10]

        return events


    class Meta:
        verbose_name = "Event List"


class EventPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('EventPage', related_name='related_links')

class EventPage(Page):
    date_from = models.DateField("Start date")
    date_to = models.DateField(
        "End date",
        null=True,
        blank=True,
        help_text="Not required if event is on a single day"
    )
    time_from = models.TimeField("Start time", null=True, blank=True)
    time_to = models.TimeField("End time", null=True, blank=True)

    location = models.CharField(max_length=255)
    description = RichTextField(blank=True)

    parent_page_types = ['EventIndexPage']

    search_fields = Page.search_fields + (
        index.SearchField('location'),
        index.SearchField('description'),
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('date_from'),
        FieldPanel('date_to'),
        FieldPanel('time_from'),
        FieldPanel('time_to'),
        FieldPanel('location'),
        FieldPanel('description', classname="full"),
        InlinePanel('related_links', label="Related links"),
    ]

    @property
    def event_index(self):
        # Find closest ancestor which is an event index
        return self.get_ancestors().type(EventIndexPage).last()

    def serve(self, request):
        if "format" in request.GET:
            if request.GET['format'] == 'ical':
                # Export to ical format
                response = HttpResponse(
                    export_event(self, 'ical'),
                    content_type='text/calendar',
                )
                response['Content-Disposition'] = 'attachment; filename=' + self.slug + '.ics'
                return response
            else:
                # Unrecognised format error
                message = 'Could not export event\n\nUnrecognised format: ' + request.GET['format']
                return HttpResponse(message, content_type='text/plain')
        else:
            # Display event page as usual
            return super(EventPage, self).serve(request)

    class Meta:
        verbose_name = "Event"


# People
# --------------------------------------------------

# class PersonPageRelatedLink(Orderable, RelatedLink):
#     page = ParentalKey('PersonPage', related_name='related_links')
#
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
        # InlinePanel('related_links', label="Related links"),
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
    parent_page_types = ['Homepage', 'StandardPage', 'PersonIndexPage']

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

class NewsArticle(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    source = models.CharField('Source Name', max_length=255, blank=True)
    source_url = models.URLField('Source URL', max_length=255, blank=True)

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
        index.SearchField('body'),
    )

    content_panels = [
        FieldPanel('title', classname="full title"),
        FieldPanel('intro', classname="full"),
        FieldPanel('body', classname="full"),
        MultiFieldPanel(
            [
                FieldPanel('source'),
                FieldPanel('source_url'),
            ],
            heading="External Source",
            classname="collapsible collapsed"
         ),
    ]
