""" Electronics models. """
from django.db import models
from apps.core.models import BaseClass

# Create your models here.


class ElectronicCategory(models.Model):
    """ Modelo de categorías para electrónicos. """
    name = models.CharField(max_length=145, null=False)

    class Meta:
        """ Verbos plurares y singurales. """
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"Categoria de electrónica: {self.name}"


class Electronic(BaseClass):
    """ Modelo para electrónicos. """
    category = models.ForeignKey(
        ElectronicCategory,
        related_name='Electronics',
        on_delete=models.SET_NULL,
        null=True
        )
