from django import template
register = template.Library()

@register.filter
def academic_range(year):
    return '{}–{}'.format(year, year + 1)
