# Generated by Django 4.2.1 on 2023-05-26 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_alter_incomingproducts_bill_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='incomingproducts',
            name='dateIncoming',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha ingreso'),
        ),
        migrations.AlterField(
            model_name='outcomingproducts',
            name='dateOutcoming',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha salida'),
        ),
    ]
