""" Vistas Users. """
from apps.users.views import login_user, logout_user, register_user
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages
from django.urls import path

urlpatterns = [
    path('login_user', login_user, name='login'),
    path('logout_user', logout_user, name='logout'),
    path('register_user', register_user, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
