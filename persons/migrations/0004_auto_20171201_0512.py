# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0003_auto_20171201_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]