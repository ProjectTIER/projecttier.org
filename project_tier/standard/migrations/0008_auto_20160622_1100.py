# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields
import wagtail.core.blocks
import wagtail.documents.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0007_auto_20160622_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardindexpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.core.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.core.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))))), ('download', wagtail.documents.blocks.DocumentChooserBlock(template='blocks/download.html', icon='fa-download')), ('accordion', wagtail.core.blocks.StructBlock((('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.core.blocks.StructBlock((('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(required=False, help_text='Choose what type of notice this is.', choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')])))))), blank=True),
        ),
        migrations.AlterField(
            model_name='standardindexpage',
            name='listing_abstract',
            field=models.TextField(blank=True, help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.'),
        ),
    ]
