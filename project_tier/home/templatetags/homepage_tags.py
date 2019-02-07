from django import template
from django.conf import settings

from project_tier.home.models import Page

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a wagtailcore.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    page = context.get('calling_page') or context.get('page')
    if page:
        return page.get_site().root_page

    return context['request'].site.root_page

def has_menu_children(page):
    return page.get_children().live().in_menu().exists()

@register.inclusion_tag('tags/standard_index_listing.html', takes_context=True)
def standard_index_listing(context, calling_page):
    pages = calling_page.get_children().live().specific()

    for page in pages:
        page.child_pages = page.get_children().in_menu().live()

    return {
        'pages': pages,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
