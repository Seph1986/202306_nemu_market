""" Motors routes. """
from apps.motor_app.views import motor_add
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
from django.urls import path

urlpatterns = [
    path('agregar/', motor_add, name='motor_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
