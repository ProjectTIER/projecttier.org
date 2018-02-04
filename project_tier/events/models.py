from __future__ import unicode_literals
from datetime import date
from django.db import models
from django.http import HttpResponse
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
)
from wagtail.search import index
from modelcluster.fields import ParentalKey
#from project_tier.links.models import RelatedLink
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


class EventPage(Page):
    date_from = models.DateField("Start date", help_text="Required for us to know if the event is in the future or past")
    date_to = models.DateField(
        "End date",
        null=True,
        blank=True,
        help_text="Not required if event is on a single day"
    )
    time_from = models.TimeField("Start time", null=True, blank=True)
    time_to = models.TimeField("End time", null=True, blank=True)

    meta_information = RichTextField(blank=True, help_text="Meta information about the event e.g. Haverford College, Department of economics")
    description = RichTextField(blank=True, help_text="The description written as though in the future")
    description_past = RichTextField(blank=True, help_text="The description written as though in the past")
    parent_page_types = ['EventIndexPage']
    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('location'),
        index.SearchField('description')
    ]

    content_panels = Page.content_panels + [
        FieldRowPanel([
            FieldPanel('date_from'),
            FieldPanel('date_to'),
        ],),
        FieldPanel('meta_information'),
        MultiFieldPanel([
            FieldPanel('description'),
            FieldPanel('description_past'),
        ], heading="Description of event"),
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
