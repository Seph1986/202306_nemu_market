""" Furnitures models. """
from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseClass

# Create your models here.


class FurnitureCategory(models.Model):
    """ Modelo de categorias para mobiliarios. """
    name = models.CharField(max_length=145, null=False)

    class Meta:
        """ Verbos plurares y singurales. """
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name}"


class Furniture(BaseClass):
    """ Modelo para mobiliarios. """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        FurnitureCategory,
        related_name='furnitures',
        on_delete=models.SET_NULL,
        null=True
        )
