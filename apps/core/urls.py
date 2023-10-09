from apps.core.views import index, search_results
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', index, name='inicio'),
    path('search/', search_results, name='search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
