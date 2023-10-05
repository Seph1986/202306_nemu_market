""" Apps.py """
from django.apps import AppConfig


class ElectronicsConfig(AppConfig):
    """ Electronics config"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.electronics"
