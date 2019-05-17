from django.test import TestCase, Client
from django.urls import reverse
from .models import Person


class PersonDetailViewTestCase(TestCase):

    def setUp(self):
        jane_doe = Person.objects.create(
            first_name="Jane",
            last_name="Doe",
            slug="jane-doe"
        )

    def test_get(self):
        """ Ensure that the page can be accessed """
        client = Client()
        response = client.get(reverse('person_detail', args=['jane-doe']))
        self.assertEqual(response.status_code, 200)
