# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20170408_1934'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='home',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
    ]