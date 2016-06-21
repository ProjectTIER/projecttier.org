# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20160613_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='personindexpage',
            name='listing_abstract',
            field=models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.', default=''),
            preserve_default=False,
        ),
    ]
