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


@register.inclusion_tag('specs/tags/specs_nav.html', takes_context=True)
def specs_nav(context, parent):

    def show_file(p):
        # TODO: Have a way to show expanded tree?
        # if 'expanded' in context['request'].GET: return True
        is_self = p.id == context['self'].id
        is_optional_file = p.__class__.__name__ == 'OptionalFilePage'
        is_parent_active = p.get_parent().id == context['self'].id
        is_sibling_active = p.get_siblings().filter(id=context['self'].id).count() > 0
        return is_self or is_parent_active or is_sibling_active or not is_optional_file

    context['parent'] = parent.specific
    context['children'] = [
        p for p in parent.get_children().specific() if show_file(p)
    ]
    return context
