from django import template
from django.urls import reverse

register = template.Library()


@register.filter
def document_view_url(value):
    return reverse('view_document', args=[value.id, value.filename])

@register.simple_tag(takes_context=True)
def pdfview(context, value):
    embed_url = "https://docs.google.com/gview?url={}&embedded=true"
    site_url = context.request.build_absolute_uri('/')[0:-1]
    pdf_url = document_view_url(value)
    return embed_url.format("{}{}".format(site_url, pdf_url))
