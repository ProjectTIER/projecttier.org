from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core.blocks import StructBlock, URLBlock, CharBlock

from project_tier.blocks import ContentStreamBlock


class SpecsPage(Page):
    """Abstract base class inherited by other spec page types."""
    body = StreamField(ContentStreamBlock(required=False), blank=True)

    content_panels = Page.content_panels + [StreamFieldPanel('body')]

    def get_context(self, request):
        context = super().get_context(request)
        context['specs_landing_page'] = SpecsLandingPage.objects.filter(page_ptr__in=self.get_ancestors(inclusive=True)).order_by('page_ptr__depth').specific().first()
        context['spec_root_page'] = context['specs_landing_page'].get_children().specific().first()

        # Prev/Next buttons
        filetree = context['specs_landing_page'].get_descendants(inclusive=True).live().specific()
        filetree_ids = [x.id for x in filetree]
        if self.id in filetree_ids:
            index = filetree_ids.index(self.id)
            try: context['next'] = filetree[index + 1]
            except Exception: pass
            try: context['prev'] = filetree[index - 1]
            except Exception: pass

        return context

    class Meta:
        abstract = True


class FolderPage(SpecsPage):
    """Represents a folder within the project hierarchy, eg: MetaData."""
    nav_icon = 'fa-folder-open'
    parent_page_types = ['specs.FolderPage', 'specs.SpecsLandingPage']
    subpage_types = [
        'specs.FolderPage', 'specs.FilePage', 'specs.OptionalFilePage'
    ]


class FilePage(SpecsPage):
    """Represents a file within the project hierarchy, eg MetaDataGuide."""
    nav_icon = 'fa-file-text'
    parent_page_types = ['specs.FolderPage']
    subpage_types = []


class OptionalFilePage(SpecsPage):
    """Optional files are ones like: 0+ existing metadata documents."""
    parent_page_types = ['specs.FolderPage']
    subpage_types = []


class SpecsLandingPage(SpecsPage):
    """Landing page for specifications"""
    body = StreamField(ContentStreamBlock())

    protocols = StreamField([
        ('protocol', StructBlock([
            ('version', CharBlock(help_text='The protocol version, such as v4.0')),
            ('link', URLBlock(help_text='Link to that version.')),
        ]))
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
        StreamFieldPanel('protocols'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['spec_root_page'] = self.get_children().specific().first()
        return context
