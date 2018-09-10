from django.urls import path
from .views import PersonDetailView

urlpatterns = [
    path('person/<slug:slug>/', PersonDetailView.as_view(), name='person_detail')
]
