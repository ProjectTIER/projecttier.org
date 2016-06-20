# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtaildocs.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('standard', '0002_auto_20160613_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, to='wagtailcore.Page', parent_link=True, serialize=False, primary_key=True)),
                ('introductory_headline', models.TextField(help_text='Introduce the topic of this page in 1-3 sentences.')),
                ('overview', wagtail.wagtailcore.fields.RichTextField(help_text='Give a general overview of what this topic is about. Limit yourself to 3 paragraphs.')),
                ('body', wagtail.wagtailcore.fields.StreamField((('section', wagtail.wagtailcore.blocks.StructBlock((('headline', wagtail.wagtailcore.blocks.TextBlock(help_text='Write a title for this section.')), ('subheadline', wagtail.wagtailcore.blocks.TextBlock(help_text='Write a subheadline for this section (optional).', required=False)), ('body', wagtail.wagtailcore.blocks.StreamBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='fa-paragraph')), ('heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/heading.html', icon='fa-header')), ('smaller_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smaller_heading.html', icon='fa-header')), ('smallest_heading', wagtail.wagtailcore.blocks.TextBlock(template='blocks/smallest_heading.html', icon='fa-header')), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False))))), ('download', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='fa-download')), ('accordion', wagtail.wagtailcore.blocks.StructBlock((('panels', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.wagtailcore.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))), label='Panel'))),))), ('notice', wagtail.wagtailcore.blocks.StructBlock((('message', wagtail.wagtailcore.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False)))))), help_text='The section content goes here.'))))),))),
                ('listing_abstract', models.TextField(help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='standardpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='StandardPage',
        ),
    ]
