""" Admin Furnitures. """
from django.contrib import admin

# Register your models here.
from .models import Furniture, FurnitureCategory

admin.site.register(Furniture)
admin.site.register(FurnitureCategory)
