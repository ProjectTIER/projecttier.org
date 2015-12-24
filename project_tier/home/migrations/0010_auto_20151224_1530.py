# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20151224_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='email',
            field=models.EmailField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='personpage',
            name='location',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='personpage',
            name='phone',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='personpage',
            name='website',
            field=models.URLField(max_length=255, blank=True),
        ),
    ]
