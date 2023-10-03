from django.db import models
from apps.core.models import BaseClass

# Create your models here.


class FurnitureCategory(models.Model):

    name = models.CharField(max_length=145, null=False)

    def __str__(self) -> str:
        return f"Categoria de muebles: {self.name}"


class Furniture(BaseClass):

    category = models.ForeignKey(
        FurnitureCategory, on_delete=models.SET_NULL, null=True)
