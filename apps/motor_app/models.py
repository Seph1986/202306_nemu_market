from django.db import models
from apps.core.models import BaseClass

# Create your models here.


class MotorCategory(models.Model):

    name = models.CharField(max_length=145)

    def __str__(self) -> str:
        return f"{self.name}"


class Motor(BaseClass):
    
    brand = models.CharField(max_length=145, null=False)
    model = models.CharField(max_length=145, null=False)
    fuel = models.CharField(max_length=50, null=False)
    transmission = models.CharField(max_length=145, null=False)
    year = models.PositiveBigIntegerField(null=False)
    color = models.CharField(max_length=50, null=False)
    images = models.FileField()
    category = models.ForeignKey(
        MotorCategory, on_delete=models.SET_NULL, null=True)

    



    def __str__(self) -> str:
        return f"{self.brand} {self.model} {self.year} {self.color} {self.transmission}"
