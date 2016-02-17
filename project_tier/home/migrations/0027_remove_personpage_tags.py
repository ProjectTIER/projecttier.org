# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_auto_20160217_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personpage',
            name='tags',
        ),
    ]
