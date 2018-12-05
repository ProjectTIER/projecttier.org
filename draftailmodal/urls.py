from django.urls import path
from . import views


# Registered with the project in wagtail_hooks.py
urlpatterns = [
    path("chooser/", views.chooser, name="draftailmodal_chooser")
]
