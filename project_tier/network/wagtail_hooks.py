from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Person


class NetworkAdmin(ModelAdmin):
    model = Person
    menu_label = 'TIER Network'  # ditch this to use verbose_name_plural from model
    menu_icon = 'user'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name', 'affiliation', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'affiliation', 'main_job_title', 'academic_title')

modeladmin_register(NetworkAdmin)
