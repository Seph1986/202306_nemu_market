from django.contrib import admin
from apps.core.models import ImageBase, BaseClass

# Core admin
class ImageBaseTabularInline(admin.TabularInline):
    """Image tabular inline admin."""

    model = ImageBase
    extra = 1


@admin.register(BaseClass)
class BaseClassAdmin(admin.ModelAdmin):
    """Base admin class."""

    # Este es el campo que permite subir más de una imagen del admin.
    inlines = [ImageBaseTabularInline]


    list_display = ('user', 'title', 'price')