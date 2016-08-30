# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0013_personpage_image_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personpage',
            name='image_credit',
            field=models.CharField(help_text="Add credit for photo if necessary. Note: add only their name 'Photo courtesy of' is hardcoded", blank=True, max_length=255),
        ),
    ]
