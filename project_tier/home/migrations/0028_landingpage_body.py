# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_remove_personpage_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
