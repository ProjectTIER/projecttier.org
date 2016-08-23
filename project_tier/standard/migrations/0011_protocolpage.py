# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('standard', '0010_auto_20160712_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtocolPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, to='wagtailcore.Page', serialize=False, primary_key=True, auto_created=True)),
                ('protocol_version', models.CharField(help_text='The version of the Protocol', blank=True, max_length=255)),
                ('listing_abstract', models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.', blank=True)),
                ('introductory_headline', models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.', blank=True)),
                ('body', wagtail.wagtailcore.fields.StreamField((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.wagtailcore.blocks.TextBlock(icon='fa-header', template='blocks/heading.html')), ('smaller_heading', wagtail.wagtailcore.blocks.TextBlock(icon='fa-header', template='blocks/smaller_heading.html')), ('smallest_heading', wagtail.wagtailcore.blocks.TextBlock(icon='fa-header', template='blocks/smallest_heading.html')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False))))), ('download', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.wagtailcore.blocks.StructBlock((('panels', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.wagtailcore.blocks.StructBlock((('message', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.wagtailcore.blocks.ChoiceBlock(help_text='Choose what type of notice this is.', choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], required=False)))))), blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
