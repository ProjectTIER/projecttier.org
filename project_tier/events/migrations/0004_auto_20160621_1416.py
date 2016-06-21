# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160621_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventpage',
            old_name='address',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='eventpage',
            old_name='location',
            new_name='university',
        ),
    ]
