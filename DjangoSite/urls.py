from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^ajax-upload/$', 'ajax_upload.views.upload', name='ajax-upload'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^files-widget/', include('topnotchdev.files_widget.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
