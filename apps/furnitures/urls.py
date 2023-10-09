""" Entertainments routes. """
from apps.furnitures.views import furniture_add, furnitures_list, edit_furniture, delete_furniture
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'furnitures'

urlpatterns = [
    path('agregar/', furniture_add, name='furniture_add'),
    path('lista/<int:id>/', furnitures_list, name='furnitures_list'),
    path('editar/<int:id>/', edit_furniture, name='edit_furniture'),
    path('eliminar/<int:id>/', delete_furniture, name='delete_furniture'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)