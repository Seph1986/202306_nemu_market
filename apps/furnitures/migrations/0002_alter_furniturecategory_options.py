# Generated by Django 4.2.5 on 2023-10-05 01:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("furnitures", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="furniturecategory",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
    ]
