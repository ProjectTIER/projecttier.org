# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20160622_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventindexpage',
            name='intro_homepage',
            field=models.TextField(help_text='Describe the events index page. This is displayed on the homepage.', blank=True),
        ),
    ]
