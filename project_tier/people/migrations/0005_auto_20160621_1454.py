# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20160621_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personindexpage',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='personindexpage',
            name='introductory_headline',
            field=models.TextField(blank=True, help_text='Introduce the topic of this page in 1-3 sentences.'),
        ),
        migrations.AddField(
            model_name='personpage',
            name='introductory_headline',
            field=models.TextField(blank=True, help_text='Introduce the topic of this page in 1-3 sentences.'),
        ),
    ]
