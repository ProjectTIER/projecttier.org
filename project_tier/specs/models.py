from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from project_tier.blocks import ContentStreamBlock


class SpecsPage(Page):
    """Abstract base class inherited by other spec page types."""
    body = StreamField(ContentStreamBlock())

    content_panels = Page.content_panels + [StreamFieldPanel('body')]

    class Meta:
        abstract = True


class FolderPage(SpecsPage):
    """Represents a folder within the project hierarchy, eg: MetaData."""
    parent_page_types = ['specs.FolderPage', 'specs.SpecsLandingPage']
    subpage_types = [
        'specs.FolderPage', 'specs.FilePage', 'specs.OptionalFilePage'
    ]


class FilePage(SpecsPage):
    """Represents a file within the project hierarchy, eg MetaDataGuide."""
    parent_page_types = ['specs.FolderPage']
    subpage_types = []


class OptionalFilePage(SpecsPage):
    """Optional files are ones like: 0+ existing metadata documents."""
    parent_page_types = ['specs.FolderPage']
    subpage_types = []


class SpecsLandingPage(SpecsPage):
    """Landing page for specifications"""
    body = StreamField(ContentStreamBlock())
