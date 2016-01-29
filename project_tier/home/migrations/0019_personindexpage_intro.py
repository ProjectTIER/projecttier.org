# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_landingpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='personindexpage',
            name='intro',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
