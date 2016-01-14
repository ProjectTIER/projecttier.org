# -*- coding: utf-8 -*-
import nose.tools as nt
import factory
from django.test import TestCase
from wagtail.tests.utils import WagtailPageTests

from project_tier.protocol.models import (ComponentIndexPage, ComponentPage,
    ProtocolHomePage)

class TestProtocolPageTests(WagtailPageTests):
    def test_assert_allowed_parent_page_types(self):
        self.assertAllowedParentPageTypes(ComponentPage, {ComponentIndexPage})
        self.assertAllowedParentPageTypes(ComponentIndexPage, {ProtocolHomePage})
    #
    # def test_assert_allowed_subpage_types(self):
    #     self.assertAllowedSubpageTypes(ProtocolHomePage, {ComponentIndexPage, StandardPage})
