from django.db import models
from apps.core.models import BaseClass

# Create your models here.


class ElectronicCategory(models.Model):

    name = models.CharField(max_length=145, null=False)

    def __str__(self) -> str:
        return f"Categoria de electrónica: {self.name}"


class Electronic(BaseClass):

    category = models.ForeignKey(
        ElectronicCategory, on_delete=models.SET_NULL, null=True)
