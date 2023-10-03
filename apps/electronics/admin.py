from django.contrib import admin

# Register your models here.
from .models import Electronic, ElectronicCategory

admin.site.register(Electronic)
admin.site.register(ElectronicCategory)
