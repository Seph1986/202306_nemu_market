from django.db import models
from apps.users.models import Profile

# Create your models here.


class BaseClass(models.Model):

    title = models.CharField(max_length=245, null=False)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    # images
    phone_number1 = models.CharField(max_length=100)
    phone_number2 = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    liked_by = models.ManyToManyField(Profile, related_name='offers')
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
