""" Entertainments models. """
from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseClass

# Create your models here.


class EntertainmentCategory(models.Model):
    """ Modelo de categorias para entretenimientos. """
    name = models.CharField(max_length=145, null=False)

    class Meta:
        """ Verbos plurares y singurales. """
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return f"{self.name}"


class Entertainment(BaseClass):
    """ Modelo para entretenimientos. """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        EntertainmentCategory,
        related_name='Entertainments',
        on_delete=models.SET_NULL,
        null=True
        )
