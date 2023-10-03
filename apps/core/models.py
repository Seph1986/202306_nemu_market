from django.db import models

# Create your models here.

class BaseClass(models.Model):

    name = models.CharField(max_length=245, null=False)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
