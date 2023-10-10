from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from apps.core.models import BaseClass
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(null=True, upload_to="images/profile_imgs", default="images/user_default_icon.png")
    favorites = models.ManyToManyField(to='core.BaseClass', related_name="users")

    def __str__(self):
        return self.user.username


def create_profle(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profle, sender=User)
