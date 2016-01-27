# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20160107_1041'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personpage',
            options={'verbose_name': 'Person', 'verbose_name_plural': 'People'},
        ),
    ]
