from django import template
from project_tier.home.models import Page
from project_tier.standard.models import StandardIndexPage, CustomIndexPage

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


def has_children(page):
    return page.get_children().live().exists()


def is_active(page, current_page):
    return (current_page.url.startswith(page.url) if current_page else False)


def get_ancestor(page):
    return page.get_ancestors(True)[2]


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('tags/table_of_contents_menu.html', takes_context=True)
def table_of_contents_menu(context, streamfield=None, pagetype=StandardIndexPage):
    page = context['page']
    section = page.get_ancestors(inclusive=True).type(pagetype).first()
    custom_section = page.get_ancestors(inclusive=True).type(CustomIndexPage).first()
    headings = []
    if streamfield:
        for block in streamfield:
            if block.block_type == 'section':
                value = block.value['headline']
                children = []
                for child in block.value['body']:
                    if child.block_type == 'heading':
                        children.append(child.value)
                headings.append({
                    'value': value,
                    'children': children,
                })
            elif block.block_type == 'heading':
                headings.append({
                    'value': block.value,
                    'children': [],
                })
            elif block.block_type == 'smaller_heading':
                try:
                    headings[-1]['children'].append(block.value)
                except:
                    pass
    return {
        'section_pages': section.get_children().specific().live() if section else None,
        'custom_section_pages': custom_section.get_children().specific().live() if custom_section else None,
        'article_headings': headings
    }


@register.inclusion_tag('tags/protocol_menu_panel.html', takes_context=True)
def protocol_menu_panel(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    for child in menuitems_children:
        child.children = child.get_children().live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=1)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }


@register.inclusion_tag('events/tags/breadcrumbs.html', takes_context=True)
def webcast_breadcrumbs(context):
    return breadcrumbs(context)


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


@register.inclusion_tag('tags/sidebar_menu.html', takes_context=True)
def sidebar_menu(context, calling_page=None):
    ancestor = get_ancestor(calling_page)
    ancestor.is_active = is_active(ancestor, calling_page)
    ancestor.has_children = has_menu_children(ancestor)

    if ancestor.has_children:
        ancestor.children = ancestor.get_children().live()

        for descendant in ancestor.children:
            descendant.is_active = is_active(descendant, calling_page)
            descendant.has_children = has_menu_children(descendant)

            if descendant.has_children:
                descendant.children = descendant.get_children().live()

    return {
        'calling_page': calling_page,
        'ancestor': ancestor,
        'request': context['request'],
    }


@register.filter()
def in_tree(page):
    ancestor = get_ancestor(page)
    return has_menu_children(ancestor)
