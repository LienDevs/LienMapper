# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 04:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lienMapper', '0003_auto_20170929_2316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='owners',
            new_name='owner',
        ),
    ]