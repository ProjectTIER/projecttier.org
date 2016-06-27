from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import NewsItem


class NewsItemModelAdmin(ModelAdmin):
    model = NewsItem
    menu_icon = 'fa-newspaper-o'
    menu_order = 200
    add_to_settings_menu = False
    list_display = ('__str__',)
    search_fields = ('__str__',)

modeladmin_register(NewsItemModelAdmin)
