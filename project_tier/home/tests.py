# -*- coding: utf-8 -*-
import nose.tools as nt
import factory
from django.test import TestCase
from project_tier.home.models import PersonPage

class PersonPageFactory(factory.DjangoModelFactory):
    class Meta:
        model = PersonPage

    location = "Office"
    phone = "2158675309"

class TestPersonPageCreation(TestCase):
  def setUp(self):
    PersonPage.get_tree().all().delete()
    self.root = PersonPage.add_root( instance=PersonPageFactory.build( title="Bob Barker") )

  def tearDown(self):
    self.root.delete()

  def test_person_page_created(self):
    nt.eq_(self.root.title, "Bob Barker")
    nt.eq_(self.root.location, "Office")
    nt.eq_(self.root.phone, "2158675309")
