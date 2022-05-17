from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class NijiUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='user/profile_picture', blank=True)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=300) 
    landmark = models.CharField(max_length=250,null=True,blank=True)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    is_lessor = models.BooleanField(default=False)
    is_lessee = models.BooleanField(default=False)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)