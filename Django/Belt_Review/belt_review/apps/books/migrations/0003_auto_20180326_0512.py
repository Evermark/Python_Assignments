# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-26 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.SmallIntegerField(),
        ),
    ]