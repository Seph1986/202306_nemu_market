""" Apps.py """
from django.apps import AppConfig


class EntertainmentConfig(AppConfig):
    """ Entertainment config. """ 
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.entertainments"
