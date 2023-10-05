""" Entertainments routes. """
from apps.entertainments.views import entertainment_add
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
from django.urls import path

urlpatterns = [
    path('agregar/', entertainment_add, name='entertainment_add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
