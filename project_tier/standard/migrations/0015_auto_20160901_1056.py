# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0014_auto_20160831_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header'))), blank=True),
        ),
    ]
