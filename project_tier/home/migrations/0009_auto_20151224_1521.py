# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_personpage_personpagerelatedlink'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventindexpage',
            options={'verbose_name': 'Event List'},
        ),
        migrations.AlterModelOptions(
            name='eventpage',
            options={'verbose_name': 'Event'},
        ),
        migrations.AlterModelOptions(
            name='personpage',
            options={'verbose_name': 'Person'},
        ),
        migrations.AlterModelOptions(
            name='standardpage',
            options={'verbose_name': 'Page'},
        ),
    ]
