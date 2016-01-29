# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_personindexpage_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='personindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
