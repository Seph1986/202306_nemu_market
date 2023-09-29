from apps.core.views import index
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('inicio/', index, name='inicio'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)