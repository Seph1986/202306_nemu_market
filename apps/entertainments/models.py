from django.db import models
from apps.core.models import BaseClass

# Create your models here.


class EntertainmentCategory(models.Model):

    name = models.CharField(max_length=145, null=False)

    def __str__(self) -> str:
        return f"Entr.: {self.name}"


class Entertainment(BaseClass):

    category = models.ForeignKey(
        EntertainmentCategory, on_delete=models.SET_NULL, null=True)
