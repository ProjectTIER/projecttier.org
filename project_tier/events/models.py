from __future__ import unicode_literals
from datetime import date
from django.db import models
from django.http import HttpResponse
from django.utils.timezone import now
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from project_tier.blocks import ContentStreamBlock
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, PageChooserPanel, StreamFieldPanel
)
from taggit.models import Tag, TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from wagtail.search import index
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
    intro_homepage = models.TextField(help_text='Describe the events index page. This is displayed on the homepage.', blank=True)

    parent_page_types = ['home.HomePage']
    subpage_types = ['events.EventPage']

    search_fields = Page.search_fields + [
        index.SearchField('intro')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('intro_homepage')
    ]

    @property
    def events(self):
        events = EventPage.objects.child_of(self).live()
        kwargs = {
            '{0}__{1}'.format('date_from', self.show_events): date.today(),
        }
        events = events.filter(**kwargs)
        events = events.order_by('date_from')
        return events

    @property
    def past_events(self):
        events = EventPage.objects.child_of(self).live().filter(date_from__lt=date.today())
        events = events.order_by('-date_from')
        events = events.all()  # [:10]
        return events

        class Meta:
            verbose_name = "Event List"

    @property
    def past_event(self):
        event = EventPage.objects.child_of(self).live().filter(date_from__lt=date.today())
        return event

    def get_context(self, request):
        past_events = self.past_events

        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(past_events, 20)

        try:
            past_events = paginator.page(page)
        except PageNotAnInteger:
            past_events = paginator.page(1)
        except EmptyPage:
            past_events = paginator.page(paginator.num_pages)

        context = super(EventIndexPage, self).get_context(request)

        # Hide upcoming events if past page 1
        if int(page) == 1:
            context['events'] = self.events

        context['past_events'] = past_events
        return context


class PartnerOrganization(models.Model):
    partner_name = models.CharField(max_length=255)
    partner_link = models.URLField("External link", blank=True)
    partner_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Partner logo, ideally square"
    )

    panels = [
        FieldPanel('partner_name'),
        FieldPanel('partner_link'),
        ImageChooserPanel('partner_logo'),
    ]

    class Meta:
        abstract = True


class EventPartnerOrganizations(Orderable, PartnerOrganization):
    event = ParentalKey('events.EventPage', on_delete=models.CASCADE, related_name='partner_organizations')


class EventTag(TaggedItemBase):
    content_object = ParentalKey(
        'events.EventPage',
        # django-modelcluster requires this to be set
        related_name='event_tags_relationship',
        on_delete=models.CASCADE
    )


class EventPage(Page):
    subtitle = models.TextField(help_text='Optional subtitle for the event', null=True, blank=True)
    date_from = models.DateField("Start date", help_text="Required for us to know if the event is in the future or past")
    date_to = models.DateField(
        "End date",
        null=True,
        blank=True,
        help_text="Not required if event is on a single day"
    )
    time_from = models.TimeField("Start time", null=True, blank=True)
    time_to = models.TimeField("End time", null=True, blank=True)
    registration_link = models.URLField(null=True, blank=True)
    location = models.TextField(help_text='Where is this event located?', null=True, blank=True)

    button_link = models.URLField(null=True, blank=True, help_text='You can put a custom link here if you want the index button to go to a different page. The default is the Registration Link, or the Event details link.')
    button_text = models.TextField(help_text='Write custom text for the index button. Default is either "Register" or "Learn More".', null=True, blank=True)

    # --- This meta_information is no longer in use!
    meta_information = RichTextField(blank=True, help_text="Meta information about the event e.g. Haverford College, Department of economics") 
    # ---

    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Ideal dimmensions are 270x180."
    )
    description = RichTextField(blank=True, help_text="The description that will appear on other pages. Keep this short and sweet.")
    description_past = RichTextField(blank=True, help_text="The description written as though in the past")
    parent_event = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="For connecting events under a larger event like a Conference or Symposium"
    )

    event_tags = ClusterTaggableManager(
        through=EventTag,
        # yes, we are really using a UUID as the related name
        related_name="+",
        blank=True,
        verbose_name="Event tags"
    )

    body = StreamField(ContentStreamBlock(required=False), blank=True)

    parent_page_types = ['EventIndexPage']
    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('description')
    ]

    content_panels = Page.content_panels + [
        
        # FieldPanel('meta_information'),
        MultiFieldPanel([
            FieldPanel('subtitle'),
            FieldRowPanel([
                FieldPanel('date_from'),
                FieldPanel('date_to'),
            ],),
            FieldRowPanel([
                FieldPanel('time_from'),
                FieldPanel('time_to'),
            ],),
            FieldPanel('location'),
            FieldRowPanel([
                FieldPanel('registration_link'),
                ImageChooserPanel('thumbnail'),
            ],),
            FieldPanel('description'),
            FieldPanel('event_tags'),
        ], heading="Basic Information"),

        StreamFieldPanel('body'),

        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('button_link'),
                FieldPanel('button_text'),
            ],),
            FieldPanel('description_past'),
            PageChooserPanel('parent_event', 'events.EventPage'),
        ], heading="Advanced Details"),

        InlinePanel('partner_organizations', label="Partner Organizations"),
    ]

    @property
    def event_index(self):
        # Find closest ancestor which is an event index
        return self.get_ancestors().type(EventIndexPage).last()

    # This is a legacy from PromptWorks. It introduces an ical download on the event page
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


class WebcastIndexPage(Page):
    intro = RichTextField(blank=True, help_text='An introductory paragraph about the webcast series')
    registration_link = models.URLField(blank=True, help_text='the Zoom registration url')
    listing_abstract = models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.', blank=True)
    subpage_types = ['events.WebcastPage']

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('listing_abstract')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('listing_abstract'),
        FieldPanel('intro'),
        FieldPanel('registration_link')
    ]

    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        context['events'] = WebcastPage.objects.child_of(self).live().order_by('date')
        return context


class WebcastPage(Page):
    date = models.DateTimeField("Event time", help_text="The time of the event")
    speaker_name = models.CharField(max_length=50, help_text="The name of the speaker")
    moderator = models.ForeignKey(
        'network.Person',
        on_delete=models.SET_NULL,
        related_name='+',
        null=True,
        blank=True,
        help_text="The moderator of the talk - TIER network person"
    )
    abstract = RichTextField(blank=True, help_text="The abstract of the talk")
    speaker_bio = RichTextField(blank=True, help_text="The bio of the event speaker")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    image_credit = models.CharField(max_length=255, blank=True, help_text="Add credit for photo if necessary. Note: add only their name 'Photo courtesy of' is hardcoded")
    video_url = models.CharField(max_length=255, blank=True)

    def status(self):
        return 'upcoming' if self.date > now() else 'ended'

    parent_page_types = ['WebcastIndexPage']
    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('abstract', 'talk_title', 'speaker_name')
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('speaker_name'),
        FieldPanel('moderator'),
        MultiFieldPanel(
            [
                ImageChooserPanel('image'),
                FieldPanel('image_credit'),
            ],
            heading="Person image"
        ),
        MultiFieldPanel([
            FieldPanel('abstract'),
            FieldPanel('speaker_bio'),
            FieldPanel('video_url'),
        ], heading="Description of event"),
    ]
