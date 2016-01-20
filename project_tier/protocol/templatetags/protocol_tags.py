from django import template
from django.conf import settings

from project_tier.protocol.models import (ProtocolHomePage, ComponentIndexPage, ComponentPage)

register = template.Library()

@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page



def has_children(page):
    return page.get_children().live().exists()

@register.inclusion_tag('tags/protocol_menu.html', takes_context=True)
def protocol_menu(context, calling_page=None):
    menuitems = calling_page.get_ancestors().type(ProtocolHomePage).last().get_children().in_menu()

    for menuitem in menuitems:
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
        menuitem.has_children = has_children(menuitem)

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
                            .type(ComponentIndexPage).last().get_children()

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
    item = ComponentPage.objects.get(pk=item.id)
    item.has_children = has_children(item)
    item.is_active = (calling_page.url.startswith(item.url)
                           if calling_page else False)

    menuitems_children = item.get_children().live().order_by('title')

    return {
        'calling_page': calling_page,
        'item': item,
        'children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }
