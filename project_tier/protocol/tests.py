# -*- coding: utf-8 -*-
import nose.tools as nt
import factory
from django.test import TestCase
from wagtail.tests.utils import WagtailPageTests

from wagtail.wagtailcore.models import Page, PageRevision, Site
from project_tier.protocol.models import (ProtocolHomePage, ComponentIndexPage, ComponentPage,
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
    title = 'Components'
    slug = 'components'
    show_in_menus = True

class ComponentPageFactory(factory.DjangoModelFactory):
    class Meta:
        model = ComponentPage
    title = 'ReadMe'
    type = 'file'
    slug = 'readme'

class TestComponentPage(TestCase):
    def setUp(self):
        self.root_page = Page.objects.get(id=3)

        self.protocol_home_page = ProtocolHomePage( title='TIER', slug='tier', show_in_menus = True )

        self.root_page.add_child( instance=self.protocol_home_page)

        self.component_index_page = ComponentIndexPageFactory.build()
        self.protocol_home_page.add_child( instance=self.component_index_page)

        self.readme_page = ComponentPageFactory.build()
        self.component_index_page.add_child( instance= self.readme_page)

    def tearDown(self):
        self.root_page.delete()

    def test_serve_component_page(self):
        response = self.client.get('/tier/components/readme/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.templates[0].name, 'protocol/component_page.html')
        readme_page = ComponentPage.objects.get(url_path='/home/tier/components/readme/')
        self.assertEqual(response.context['self'], readme_page)

        self.assertContains(response, '<h2>ReadMe</h2>')
        self.assertContains(response, '<nav id="protocol-menu">')
        self.assertContains(response, '<nav id="component-menu">')
