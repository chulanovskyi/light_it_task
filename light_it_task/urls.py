"""
https://docs.djangoproject.com/en/1.10/topics/http/urls/
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    url(r'^core/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('tournament.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
