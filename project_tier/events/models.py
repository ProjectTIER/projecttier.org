from __future__ import unicode_literals
from datetime import date
from django.db import models
from django.http import HttpResponse
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, InlinePanel, MultiFieldPanel
)
from wagtail.wagtailsearch import index
from modelcluster.fields import ParentalKey
from project_tier.links.models import RelatedLink


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

    parent_page_types = ['home.HomePage']

    search_fields = Page.search_fields + (
        index.SearchField('intro'),
    )

    content_panels = [
        FieldPanel('title', classname="title"),
        FieldPanel('intro', classname="full"),
        FieldPanel('show_events', classname="")
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

    description = RichTextField(blank=True)
    university = models.CharField(max_length=255)
    department = RichTextField(blank=True)

    parent_page_types = ['EventIndexPage']
    subpage_types = []

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
        MultiFieldPanel([
            FieldPanel('university'),
            FieldPanel('department'),
        ], heading="Address"),
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
