# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_book_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='library.Place')),
                ('serves_hot_dogs', models.BooleanField(default=False)),
                ('serves_pizza', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='waiter',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Restaurant'),
        ),
    ]
