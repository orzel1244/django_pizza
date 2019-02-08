# Generated by Django 2.0.10 on 2019-02-05 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingradient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=30)),
                ('building_number', models.IntegerField()),
                ('end_time', models.DateTimeField(blank=True, editable=False, null=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('comment', models.TextField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('ingradients', models.ManyToManyField(related_name='ingradients', to='pizza.Ingradient')),
            ],
        ),
        migrations.CreateModel(
            name='Quanity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quanitity', models.IntegerField(default=1, verbose_name='Ilosc')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Order', verbose_name='Zamówienie')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Pizza', verbose_name='Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pizzas',
            field=models.ManyToManyField(related_name='pizzas', through='pizza.Quanity', to='pizza.Pizza'),
        ),
    ]
