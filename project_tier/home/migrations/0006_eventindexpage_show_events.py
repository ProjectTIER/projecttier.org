# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_standardpage_standardpagerelatedlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventindexpage',
            name='show_events',
            field=models.CharField(default='gte', max_length=3, choices=[('gte', 'Upcoming Events'), ('lt', 'Past Events')]),
        ),
    ]
