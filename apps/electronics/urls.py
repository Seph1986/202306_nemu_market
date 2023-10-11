""" Electronics routes. """
from apps.electronics.views import electronic_add, electronics_list, edit_electronic, delete_electronic
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'electronics'

urlpatterns = [
    path('agregar/', electronic_add, name='electronic_add'),
    path('lista/<int:id>/', electronics_list, name='electronics_list'),
    path('editar/<int:id>/', edit_electronic, name='edit_electronic'),
    path('eliminar/<int:id>/', delete_electronic, name='delete_electronic'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
