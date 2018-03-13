from django.urls import include, path, re_path
from django.conf import settings
from django.contrib import admin
from project_tier.search.views import search
from project_tier.core.views import view_document


urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include('wagtail.admin.urls')),
    path('documents/', include('wagtail.documents.urls')),

    re_path(r'^document/view/(\d+)/(.*)$', view_document, name='view_document'),  # noqa

    path('search/', search, name='search'),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.views.generic import TemplateView

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Add views for testing 404 and 500 templates
    urlpatterns += [
        path('test404/', TemplateView.as_view(template_name='404.html')),
        path('test500/', TemplateView.as_view(template_name='500.html')),
    ]

urlpatterns += [
    path('', include('wagtail.core.urls')),
]
