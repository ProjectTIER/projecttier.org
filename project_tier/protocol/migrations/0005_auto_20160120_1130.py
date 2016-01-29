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
        ('protocol', '0004_auto_20160115_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocolprocesssection',
            name='page',
        ),
        migrations.AddField(
            model_name='protocolprocesspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', label='Section Title', icon='title')), (b'h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), (b'reference_page', wagtail.wagtailcore.blocks.PageChooserBlock(icon='doc-full')), (b'embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), (b'aligned_image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock()), (b'alignment', project_tier.protocol.models.ImageFormatChoiceBlock())], icon='image', label='Aligned image')), (b'document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse'))], default=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ProtocolProcessSection',
        ),
    ]
