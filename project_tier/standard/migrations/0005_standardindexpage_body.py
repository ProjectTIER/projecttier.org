# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.images.blocks
import wagtail.documents.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0004_standardpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardindexpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/heading.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', template='blocks/smallest_heading.html')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))))), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download')), ('accordion', wagtail.core.blocks.StructBlock((('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.core.blocks.StructBlock((('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(required=False, choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.')))))), default=''),
            preserve_default=False,
        ),
    ]
