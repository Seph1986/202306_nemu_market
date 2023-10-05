""" Admin Entertainments. """
from django.contrib import admin

# Register your models here.
from .models import Entertainment, EntertainmentCategory

admin.site.register(Entertainment)
admin.site.register(EntertainmentCategory)
