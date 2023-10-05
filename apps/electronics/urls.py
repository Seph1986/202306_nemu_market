""" Electronics routes. """
from apps.electronics.views import electronic_add
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
from django.urls import path

urlpatterns = [
    path('agregar/', electronic_add, name='electronic_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
