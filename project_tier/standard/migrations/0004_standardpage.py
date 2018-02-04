# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.core.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('standard', '0003_auto_20160620_1426'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, auto_created=True, to='wagtailcore.Page', primary_key=True, serialize=False, parent_link=True)),
                ('introductory_headline', models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.')),
                ('overview', wagtail.core.fields.RichTextField(help_text='Give a general overview of what this topic is about. Limit yourself to 3 paragraphs.')),
                ('body', wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.core.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.core.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.core.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.core.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))))), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download')), ('accordion', wagtail.core.blocks.StructBlock((('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.core.blocks.StructBlock((('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(help_text='Choose what type of notice this is.', required=False, choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')])))))))),
                ('listing_abstract', models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
