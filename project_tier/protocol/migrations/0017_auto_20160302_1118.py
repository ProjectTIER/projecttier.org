# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import project_tier.protocol.models


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0016_auto_20160302_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentpage',
            name='description',
        ),
    ]
