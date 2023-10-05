""" Admin Motors. """
from django.contrib import admin

# Register your models here.
from .models import Motor, MotorCategory

admin.site.register(Motor)
admin.site.register(MotorCategory)
