# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0012_auto_20160823_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sectionpage',
            options={'verbose_name': 'Standard page with content sections'},
        ),
    ]
