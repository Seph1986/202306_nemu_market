from apps.users.views import login
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('login/', login, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
