from django.contrib import admin
from django.views.static import serve
from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path("admin_panel/", admin.site.urls),
    path("", include('group_auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

