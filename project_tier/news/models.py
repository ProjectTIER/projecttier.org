from wagtail.wagtailcore.models import Orderable
from wagtail.wagtailcore.fields import RichTextField
from django.utils.html import strip_tags


class NewsItem(Orderable):
    body = RichTextField()

    def __str__(self):
        return strip_tags(self.body)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news items'
