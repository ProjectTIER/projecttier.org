# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0010_auto_20160621_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='fellowshipsindexpage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='fellowshipsindexpage',
            name='introductory_headline',
            field=models.TextField(blank=True, help_text='Introduce the topic of this page in 1-3 sentences.'),
        ),
        migrations.AddField(
            model_name='fellowshipsindexpage',
            name='listing_abstract',
            field=models.TextField(default='', help_text='Give a brief blurb (about 1 sentence) of what this topic is about. It will appear on other pages that refer to this one.'),
            preserve_default=False,
        ),
    ]
