# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Annotation', '0005_auto_20160615_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagesequence',
            name='nr_of_frames',
            field=models.PositiveIntegerField(default=298),
            preserve_default=False,
        ),
    ]