# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsitem',
            options={'verbose_name': 'news', 'verbose_name_plural': 'news'},
        ),
    ]
