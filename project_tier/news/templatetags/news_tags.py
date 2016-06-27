from django import template
from django.conf import settings
from project_tier.news.models import NewsItem

register = template.Library()

@register.inclusion_tag('news/tags/news_listing.html')
def news_listing():
    return {
        'news_items': NewsItem.objects.all()
    }
