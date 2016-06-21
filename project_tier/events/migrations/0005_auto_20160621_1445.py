# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20160621_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='department',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
