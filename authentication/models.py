from django.contrib.auth.models import AbstractUser
from django.db import models
# from django import forms


class User(AbstractUser):
  #   SUBSCRIBER = 'SUBSCRIBER'
#
   # ROLE_CHOICES = (
  #       (SUBSCRIBER, 'Subscriber'),
#    )

    username = models.CharField('Usuario',max_length=30, unique=True)
    nombre = models.CharField(max_length=10,null=True)
    email = models.EmailField('E-mail', unique=True)
    profile_photo = models.ImageField()
    role = models.CharField(max_length=30,blank=True)
    phone_number = models.CharField('Telefono',max_length=10,null=True)
    password = models.CharField('Contraseña',max_length=128)
