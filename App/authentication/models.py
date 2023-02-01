from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group
# from django import forms
from django.utils import timezone
import datetime
import random


class User(AbstractUser):
    ADMIN = 'ADMIN'
    CLIENTE = 'CLIENTE'
    GERENTE = 'GERENTE'
    OPERADOR = 'OPERADOR'
  
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CLIENTE, 'Cliente'),
        (GERENTE, 'Gerente'),
        (OPERADOR, 'Operador'),

    )

    NATURAL = 'NATURAL'
    EMPRESA = 'EMPRESA'

    CAT_CHOICES = ((NATURAL, 'Natural'), 
     (EMPRESA, 'Empresa'),
    )

    PAGO = 'PAGO'
    NO_PAGO = 'NO PAGO'

    PAY_CHOICES = ((PAGO, 'Pago'), 
     (NO_PAGO, 'No pago'),
    )

    username = models.CharField('Usuario',max_length=30, unique=True)
    nombre = models.CharField(max_length=30,null=True)
    email = models.EmailField('E-mail', unique=True)
    role = models.CharField(max_length=30,blank=True, default='CLIENTE')
    phone_number = models.CharField('Telefono',max_length=10,null=True)
    password = models.CharField('Contraseña',max_length=128)
    direccion = models.CharField(max_length=30,null=True)
    categoria = models.CharField(max_length=30,blank=True)

class Factura(models.Model):
    cliente = models.CharField('Usuario',max_length=30, unique=False)
    fecha_facturacion = models.DateField(default=datetime.datetime.now)
    fecha_vencimiento = models.DateField(default=datetime.datetime.now)
    consumo = models.FloatField(blank=True, null=True)
    total_pagar = models.FloatField(blank=True)
    Pagado = models.CharField(max_length=10,null=True, default= 'false')

    def save(self, *args, **kwargs):
        if not (self.total_pagar and self.consumo) :
            self.consumo = random.uniform(100, 400)
            self.total_pagar = self.consumo*1024
        super().save(*args, **kwargs)
