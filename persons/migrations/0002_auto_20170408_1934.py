# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-08 15:04
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='home',
            managers=[
                ('objectsvotable', django.db.models.manager.Manager()),
            ],
        ),
    ]
