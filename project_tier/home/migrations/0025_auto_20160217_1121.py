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
        ('home', '0023_remove_newsarticle_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standardpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='standardpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='StandardPageRelatedLink',
        ),
    ]
