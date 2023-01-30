from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import Group
# from django import forms
from django.utils import timezone


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
    role = models.CharField(max_length=30,blank=True)
    phone_number = models.CharField('Telefono',max_length=10,null=True)
    password = models.CharField('Contraseña',max_length=128)
    direccion = models.CharField(max_length=30,null=True)
    categoria = models.CharField(max_length=30,blank=True)


class Factura(models.Model):
    cliente = models.CharField('Usuario',max_length=30, unique=False)
    fecha_facturacion = models.TimeField(default=timezone.now)
    fecha_vencimiento = models.TimeField(default=timezone.now)
    total_pagar = models.IntegerField()
    consumo = models.IntegerField()
    Pagado = models.CharField(max_length=10,null=True)
