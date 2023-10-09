""" Entertainments routes. """
from apps.entertainments.views import entertainment_add, entertainments_list, delete_entertainment
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'entertainments'

urlpatterns = [
    path('agregar/', entertainment_add, name='entertainment_add'),
    path('lista/<int:id>/', entertainments_list, name='entertainments_list'),
    path('eliminar/<int:id>/', delete_entertainment, name='delete_entertainment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
