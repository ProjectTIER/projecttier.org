# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0015_auto_20160901_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardindexpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html'))), blank=True),
        ),
    ]
