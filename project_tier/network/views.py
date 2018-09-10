from django.views.generic import DetailView
from .models import Person

class PersonDetailView(DetailView):
    model = Person
