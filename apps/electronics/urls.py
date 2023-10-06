""" Electronics routes. """
from apps.electronics.views import electronic_add, electronics_list
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
from django.urls import path

app_name = 'electronics'

urlpatterns = [
    path('agregar/', electronic_add, name='electronic_add'),
    path('lista/<int:id>/', electronics_list, name='electronics_list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
