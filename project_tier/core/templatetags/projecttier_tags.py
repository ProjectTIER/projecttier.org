from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def document_view_url(value):
    return reverse('view_document', args=[value.id, value.filename])
