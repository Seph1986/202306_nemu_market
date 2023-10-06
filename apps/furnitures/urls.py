""" Entertainments routes. """
from apps.furnitures.views import furniture_add, furnitures_list
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
from django.urls import path

app_name = 'furnitures'

urlpatterns = [
    path('agregar/', furniture_add, name='furniture_add'),
    path('lista/<int:id>/', furnitures_list, name='furnitures_list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)