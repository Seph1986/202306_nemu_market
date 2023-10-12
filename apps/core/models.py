from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BaseClass(models.Model):

    user = models.ForeignKey(User, related_name='publication', on_delete=models.CASCADE)
    title = models.CharField(max_length=245, null=False)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    # images
    phone_number1 = models.CharField(max_length=100)
    phone_number2 = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True)
    #FAVORITES = MANY TO MANY WITH USERS
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)


class ImageBase(models.Model):
    """Modelo para las imagenes de los productos."""

    image = models.ImageField(upload_to='publication_images/')
    product = models.ForeignKey(to=BaseClass, on_delete=models.CASCADE, related_name='images')