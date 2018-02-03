# -*- coding: utf-8 -*-
from project_tier.home.models import HomePage
from project_tier.events.models import EventPage, EventIndexPage
from project_tier.people.models import PersonPage, PersonIndexPage
from project_tier.standard.models import StandardPage
from wagtail.tests.utils import WagtailPageTests


class TestPageTests(WagtailPageTests):
    def test_assert_allowed_parent_page_types(self):
        self.assertAllowedParentPageTypes(
            EventIndexPage, {HomePage, StandardPage})
        self.assertAllowedParentPageTypes(
            PersonIndexPage, {HomePage, StandardPage, PersonIndexPage})
        self.assertAllowedParentPageTypes(EventPage, {EventIndexPage})
        self.assertAllowedParentPageTypes(PersonPage, {PersonIndexPage})
