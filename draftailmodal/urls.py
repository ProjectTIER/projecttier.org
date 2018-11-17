from django.urls import path
from . import views


urlpatterns = [
    path("chooser/", views.chooser, name="draftailmodal_chooser")
]
