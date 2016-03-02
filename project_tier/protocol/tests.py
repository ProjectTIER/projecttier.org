# -*- coding: utf-8 -*-
import nose.tools as nt
import factory
from django.test import TestCase
from wagtail.tests.utils import WagtailPageTests

from wagtail.wagtailcore.models import Page, PageRevision, Site
from project_tier.protocol.models import (ProtocolHomePage, ComponentIndexPage, ComponentPage,
    ProtocolProcessPage)
from project_tier.home.models import (StandardPage)

class TestProtocolPageTests(WagtailPageTests):
    def test_assert_allowed_parent_page_types(self):
        self.assertAllowedParentPageTypes(ComponentPage, {ComponentIndexPage, ComponentPage, StandardPage})
        self.assertAllowedParentPageTypes(ComponentIndexPage, {ProtocolHomePage})
        self.assertAllowedParentPageTypes(ProtocolProcessPage, {ProtocolProcessPage, ProtocolHomePage})
    #
    # def test_assert_allowed_subpage_types(self):
    #     self.assertAllowedSubpageTypes(ProtocolHomePage, {ComponentIndexPage, StandardPage})
