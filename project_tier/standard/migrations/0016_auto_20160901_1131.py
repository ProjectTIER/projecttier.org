# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0015_auto_20160901_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph')), ('smaller_heading', wagtail.wagtailcore.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html'))), blank=True),
        ),
    ]
