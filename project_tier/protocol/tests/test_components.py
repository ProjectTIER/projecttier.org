# -*- coding: utf-8 -*-
import nose.tools as nt
import factory
from django.test import TestCase
from wagtail.tests.utils import WagtailPageTests

from wagtail.wagtailcore.models import Page, PageRevision, Site
from project_tier.protocol.models import (ProtocolHomePage, ComponentIndexPage, ComponentPage,
    ProtocolProcessPage)

class ComponentIndexPageFactory(factory.DjangoModelFactory):
    class Meta:
        model = ComponentIndexPage
    title = 'Components'
    intro = '<p>Its a pizza party!</p>'
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
        # self.site = Site.objects.get(is_default_site=True)
        self.root_page = Page.objects.get(id=3)

        self.protocol_home_page = ProtocolHomePage( title='TIER', slug='tier', show_in_menus = True )

        self.root_page.add_child( instance=self.protocol_home_page)

        self.component_index_page = ComponentIndexPageFactory.build()
        self.protocol_home_page.add_child( instance=self.component_index_page)

        self.readme_page = ComponentPageFactory.build()
        self.component_index_page.add_child( instance= self.readme_page)

    def tearDown(self):
        self.root_page.delete()

    def test_protocol_menu(self):
        response = self.client.get('/tier/components/readme/')
        self.assertContains(response, 'data-test-id="protocol-nav"')
        self.assertContains(response, '<a href="/tier/components/">Components</a>')

    def test_component_menu(self):
        response = self.client.get('/tier/components/readme/')
        self.assertContains(response, 'data-test-id="component-nav"')
        self.assertContains(response, '<a class="component-menu-item" href="/tier/components/readme/">')
        self.assertContains(response, '<li class="component-file active">')

    def test_serve_component_page(self):
        response = self.client.get('/tier/components/readme/')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.templates[0].name, 'protocol/component_page.html')
        readme_page = ComponentPage.objects.get(url_path='/home/tier/components/readme/')
        self.assertEqual(response.context['self'], readme_page)

        self.assertContains(response, '<h2 data-test-id="component-title-ReadMe">')
        self.assertContains(response, '<div class="page-intro">')
