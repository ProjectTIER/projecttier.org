# -*- coding: utf-8 -*-
import nose.tools as nt
import factory
from django.test import TestCase
from wagtail.tests.utils import WagtailPageTests

from project_tier.protocol.models import (ComponentIndexPage, ComponentPage,
    ProtocolHomePage)

class TestProtocolPageTests(WagtailPageTests):
    def test_assert_allowed_parent_page_types(self):
        self.assertAllowedParentPageTypes(ComponentPage, {ComponentIndexPage, ComponentPage})
        self.assertAllowedParentPageTypes(ComponentIndexPage, {ProtocolHomePage})
    #
    # def test_assert_allowed_subpage_types(self):
    #     self.assertAllowedSubpageTypes(ProtocolHomePage, {ComponentIndexPage, StandardPage})

class ComponentIndexPageFactory(factory.DjangoModelFactory):
    class Meta:
        model = ComponentIndexPage
    title = "Components"

class ComponentPageFactory(factory.DjangoModelFactory):
    class Meta:
        model = ComponentPage
    title = "Component"

class TestComponentPage(TestCase):
  def setUp(self):
    self.root = ComponentIndexPage.add_root(instance=ComponentIndexPageFactory.build())
    self.root.add_child(instance=ComponentPageFactory.build())

  def tearDown(self):
    self.root.delete()

  def test_person_page_created(self):
    nt.eq_(self.root.title, "Components")
