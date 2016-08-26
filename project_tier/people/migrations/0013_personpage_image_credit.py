# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0012_auto_20160823_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='personpage',
            name='image_credit',
            field=models.CharField(max_length=255, help_text='Add credit for photo if necessary', blank=True),
        ),
    ]
