from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    #phone = PhoneField(blank=True, max_length=11, help_text='Contact phone number')

    email = models.EmailField(max_length=255, null=False)
    phone = models.CharField(max_length=11, unique=True, null=False, blank=False)
    password = models.CharField(max_length=50)
    # email_confirmed = models.BooleanField(default=False)

    # @receiver(post_save, sender=User)
    # def update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         CustomUser.objects.create(user=instance)
    #     instance.profile.save()
