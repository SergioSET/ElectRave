# Generated by Django 4.1.4 on 2023-01-29 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_factura_user_categoria_user_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='Pagado',
            field=models.CharField(max_length=10, null=True),
        ),
    ]