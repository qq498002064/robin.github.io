# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 02:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_auto_20170214_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowing',
            old_name='reader_id',
            new_name='reader',
        ),
    ]
