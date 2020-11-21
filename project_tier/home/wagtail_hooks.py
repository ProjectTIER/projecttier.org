from django.utils.html import format_html, format_html_join
from django.conf import settings
from wagtail.core import hooks


@hooks.register('insert_editor_js')
def editor_js():
    js_files = [
        'js/hallo.js',
    ]
    js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )
    return js_includes + format_html(
        """
        <script>
            registerHalloPlugin('inlineonly');
        </script>
        """
    )

@hooks.register('insert_editor_css')
def admin_css():
    return format_html(
        '<link rel="stylesheet" href="' + settings.STATIC_URL + 'css/admin.css">'
    )


@hooks.register("construct_page_chooser_queryset")
def fix_page_sorting(pages, request):
    pages = pages.order_by("-latest_revision_created_at")
    return pages
