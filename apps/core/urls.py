from apps.core.views import index, search_results, favorite_control, show_detail
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', index, name='inicio'),
    path('search/', search_results, name='search_results'),
    path('favorito/<int:id>', favorite_control, name='favorite_control'),
    path('detalle/<int:id>', show_detail, name='show_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
