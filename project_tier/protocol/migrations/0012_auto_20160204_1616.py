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
        ('protocol', '0011_auto_20160204_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolprocesspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', label='Section Title', icon='title')), (b'h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'reference_page', wagtail.wagtailcore.blocks.PageChooserBlock(icon='doc-full')), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), (b'aligned_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock()), (b'alignment', project_tier.protocol.models.ImageFormatChoiceBlock())], icon='image', label='Aligned image')), (b'tip', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(label='Tip Heading')), (b'details', wagtail.wagtailcore.blocks.RichTextBlock())], icon='help', label='Tip')), (b'extended_info', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(help_text='The heading of an extended info setting', label='Heading')), (b'details', wagtail.wagtailcore.blocks.RichTextBlock())], icon='plus-inverse', label='Extended Info')), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))]),
        ),
    ]
