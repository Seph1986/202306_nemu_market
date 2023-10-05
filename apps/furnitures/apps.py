""" Apps.py """
from django.apps import AppConfig


class FurnitureConfig(AppConfig):
    """ Furnitures config. """
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.furnitures"
