# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0007_auto_20160622_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='standardindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False))))), ('download', wagtail.wagtaildocs.blocks.DocumentChooserBlock(template='blocks/download.html', icon='fa-download')), ('accordion', wagtail.wagtailcore.blocks.StructBlock((('panels', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.wagtailcore.blocks.StructBlock((('message', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.wagtailcore.blocks.ChoiceBlock(required=False, help_text='Choose what type of notice this is.', choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')])))))), blank=True),
        ),
        migrations.AlterField(
            model_name='standardindexpage',
            name='listing_abstract',
            field=models.TextField(blank=True, help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.'),
        ),
    ]
