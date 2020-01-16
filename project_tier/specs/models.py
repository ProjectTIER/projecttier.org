from django.db import models
from wagtail.core.models import Page


class SpecsPage(Page):
    # TODO: https://github.com/ProjectTIER/projecttier.org/issues/121
    class Meta:
        abstract = True


class FolderPage(SpecsPage):
    # TODO: https://github.com/ProjectTIER/projecttier.org/issues/122
    pass


class FilePage(SpecsPage):
    # TODO: https://github.com/ProjectTIER/projecttier.org/issues/123
    pass


class OptionalFilePage(SpecsPage):
    # TODO: https://github.com/ProjectTIER/projecttier.org/issues/124
    pass


class SpecsLandingPage(SpecsPage):
    # TODO: https://github.com/ProjectTIER/projecttier.org/issues/125
    pass
