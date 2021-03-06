# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-16 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20181116_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rated_project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_rating',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Rating'),
        ),
    ]
