# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailembeds.blocks
import wagtail.wagtaildocs.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0013_auto_20160826_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('section', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.TextBlock(help_text='Write a title for this section.')), ('subheadline', wagtail.wagtailcore.blocks.TextBlock(required=False, help_text='Write a subheadline for this section (optional).')), ('body', wagtail.wagtailcore.blocks.StreamBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False))))), ('download', wagtail.wagtaildocs.blocks.DocumentChooserBlock(template='blocks/download.html', icon='fa-download')), ('accordion', wagtail.wagtailcore.blocks.StructBlock((('panels', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.wagtailcore.blocks.StructBlock((('message', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], required=False, help_text='Choose what type of notice this is.'))))), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media'))), help_text='The section content goes here.'))))),)),
        ),
        migrations.AlterField(
            model_name='standardindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False))))), ('download', wagtail.wagtaildocs.blocks.DocumentChooserBlock(template='blocks/download.html', icon='fa-download')), ('accordion', wagtail.wagtailcore.blocks.StructBlock((('panels', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.wagtailcore.blocks.StructBlock((('message', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], required=False, help_text='Choose what type of notice this is.'))))), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media'))), blank=True),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False))))), ('download', wagtail.wagtaildocs.blocks.DocumentChooserBlock(template='blocks/download.html', icon='fa-download')), ('accordion', wagtail.wagtailcore.blocks.StructBlock((('panels', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.wagtailcore.blocks.StructBlock((('message', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], required=False, help_text='Choose what type of notice this is.'))))), ('embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')))),
        ),
    ]
