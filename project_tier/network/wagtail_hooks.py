from wagtail.core.models import Page
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel
)
import datetime
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel
)
from wagtail.images.edit_handlers import ImageChooserPanel
from .models import Person


class NetworkAdmin(ModelAdmin):
    model = Person
    menu_label = 'TIER Network'  # ditch this to use verbose_name_plural from model
    menu_icon = 'user'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('first_name', 'last_name', 'affiliation', 'categories')
    list_filter = ('categories',)
    search_fields = ('first_name', 'last_name', 'affiliation',
                     'main_job_title', 'secondary_job_title', 'tier_title')

modeladmin_register(NetworkAdmin)
