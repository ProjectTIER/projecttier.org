from django import template
from django.urls import reverse
from django.conf import settings

register = template.Library()


@register.filter
def document_view_url(value):
    return reverse('view_document', args=[value.id, value.filename])


@register.simple_tag
def get_setting(name):
    return getattr(settings, name, "")
