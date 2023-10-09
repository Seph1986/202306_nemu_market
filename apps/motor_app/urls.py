""" Motors routes. """
from apps.motor_app.views import motor_add, motor_app_list, delete_motor_app
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'motor_app'

urlpatterns = [
    path('agregar/', motor_add, name='motor_add'),
    path('lista/<int:id>/', motor_app_list, name='motor_app_list'),
    path('eliminar/<int:id>/', delete_motor_app, name='delete_motor_app'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
