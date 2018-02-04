# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.embeds.blocks
import wagtail.documents.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0013_auto_20160826_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpage',
            name='body',
            field=wagtail.core.fields.StreamField((('section', wagtail.core.blocks.StructBlock((('headline', wagtail.core.blocks.TextBlock(help_text='Write a title for this section.')), ('subheadline', wagtail.core.blocks.TextBlock(required=False, help_text='Write a subheadline for this section (optional).')), ('body', wagtail.core.blocks.StreamBlock((('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.core.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.core.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))))), ('download', wagtail.documents.blocks.DocumentChooserBlock(template='blocks/download.html', icon='fa-download')), ('accordion', wagtail.core.blocks.StructBlock((('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.core.blocks.StructBlock((('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], required=False, help_text='Choose what type of notice this is.'))))), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media'))), help_text='The section content goes here.'))))),)),
        ),
        migrations.AlterField(
            model_name='standardindexpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.core.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.core.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))))), ('download', wagtail.documents.blocks.DocumentChooserBlock(template='blocks/download.html', icon='fa-download')), ('accordion', wagtail.core.blocks.StructBlock((('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.core.blocks.StructBlock((('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], required=False, help_text='Choose what type of notice this is.'))))), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media'))), blank=True),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.core.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.core.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))))), ('download', wagtail.documents.blocks.DocumentChooserBlock(template='blocks/download.html', icon='fa-download')), ('accordion', wagtail.core.blocks.StructBlock((('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.core.blocks.StructBlock((('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], required=False, help_text='Choose what type of notice this is.'))))), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')))),
        ),
    ]
