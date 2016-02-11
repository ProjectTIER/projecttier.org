from django import template
from django.conf import settings
import re

from project_tier.protocol.models import (ProtocolProcessPage, ProtocolHomePage,
                                         ComponentIndexPage, ComponentPage)

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page

def has_children(page):
    return page.get_children().live().exists()

def has_children_in_menu(page):
    return page.get_children().live().in_menu().exists()

def is_active(page, current_page):
    return (current_page.url == page.url if current_page else False)

def is_active_tree(page, current_page):
    return (current_page.url.startswith(page.url) if current_page else False)


@register.inclusion_tag('tags/protocol_menu.html', takes_context=True)
def protocol_menu(context, calling_page=None):
    menuitems = calling_page.get_ancestors().type(ProtocolHomePage).last().get_children().in_menu()

    for menuitem in menuitems:
        menuitem.is_active = is_active_tree(menuitem, calling_page)
        menuitem.has_children = has_children_in_menu(menuitem)

        if menuitem.has_children:
            menuitem.children = menuitem.get_children().live().order_by('title')


    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        'request': context['request'],
    }

@register.inclusion_tag('tags/component_menu.html', takes_context=True)
def component_menu(context, calling_page):
    menuitems = calling_page.get_ancestors().type(ProtocolHomePage).last().get_children() \
                            .type(ComponentIndexPage).last().get_children().specific()

    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('tags/component_menu_item.html', takes_context=True)
def component_menu_item(context, item, calling_page=None):
    # Not sure item is just a Page instead of a ComponentPage. I need it's type
    item.has_children = has_children(item)
    item.is_active = is_active(item, calling_page)

    menuitems_children = item.get_children().specific().live().order_by('title')

    return {
        'calling_page': calling_page,
        'item': item,
        'children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }

@register.simple_tag()
def component_icon(type):
    if type == 'folder':
        icon = 'fa-folder-open-o'
    elif type == 'data':
        icon = 'fa-table'
    elif type == 'multiple':
        icon = 'fa-files-o'
    else:
        icon = 'fa-file-text-o'
    return icon


@register.simple_tag()
def dump(var):
    return vars(var)

@register.simple_tag()
def dasherize(str):
    str = re.sub('[^A-Za-z0-9\s]+', '', str)
    return str.lower().replace(' ', '-')
