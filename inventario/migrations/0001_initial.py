# Generated by Django 4.2.1 on 2023-05-17 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=400)),
                ('category', models.CharField(choices=[('0', 'Árboles y arbustos'), ('1', 'Césped y tapizantes'), ('2', 'Anuales'), ('3', 'Bulbosas'), ('4', 'Palmeras'), ('5', 'Helechos'), ('6', 'Trepadoras'), ('7', 'Acuáticas')], max_length=1, verbose_name='Categoría')),
                ('initial_stock', models.IntegerField()),
                ('incomings', models.IntegerField()),
                ('outcomings', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='outcomingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.CharField(max_length=10)),
                ('dateOutcoming', models.DateTimeField()),
                ('quantityOutcoming', models.IntegerField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.productsmodel', verbose_name='Productos')),
            ],
        ),
        migrations.CreateModel(
            name='incomingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.CharField(max_length=10)),
                ('dateIncoming', models.DateTimeField()),
                ('quantityIncoming', models.IntegerField()),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.productsmodel', verbose_name='Productos')),
            ],
        ),
    ]