# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('standard', '0005_standardindexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionpage',
            name='introductory_headline',
            field=models.TextField(blank=True, help_text='Introduce the topic of this page in 1-3 sentences.'),
        ),
        migrations.AlterField(
            model_name='sectionpage',
            name='overview',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Give a general overview of what this topic is about. Limit yourself to 3 paragraphs.'),
        ),
        migrations.AlterField(
            model_name='standardindexpage',
            name='introductory_headline',
            field=models.TextField(blank=True, help_text='Introduce the topic of this page in 1-3 sentences.'),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='introductory_headline',
            field=models.TextField(blank=True, help_text='Introduce the topic of this page in 1-3 sentences.'),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='overview',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Give a general overview of what this topic is about. Limit yourself to 3 paragraphs.'),
        ),
    ]
