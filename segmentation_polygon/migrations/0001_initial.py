# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-10-08 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('annotationweb', '0019_auto_20181008_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControlPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('index', models.PositiveIntegerField()),
                ('frame', models.PositiveIntegerField()),
                ('object', models.PositiveIntegerField()),
                ('uncertain', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SegmentationPolygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frames', models.TextField()),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='annotationweb.ProcessedImage')),
            ],
        ),
        migrations.AddField(
            model_name='controlpoint',
            name='segmentation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segmentation_polygon.SegmentationPolygon'),
        ),
    ]