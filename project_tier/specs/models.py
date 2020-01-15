from django.db import models
from wagtail.core.models import Page


class SpecsPage(Page):
    class Meta:
        abstract = True


class FolderPage(SpecsPage):
    pass


class FilePage(SpecsPage):
    pass


class OptionalFilePage(SpecsPage):
    pass


class SpecsLandingPage(SpecsPage):
    pass
