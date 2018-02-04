# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20160621_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventpagerelatedlink',
            name='page',
        ),
        migrations.AddField(
            model_name='eventpage',
            name='meta_information',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Meta information about the event e.g. Haverford College, Department of economics'),
        ),
        migrations.DeleteModel(
            name='EventPageRelatedLink',
        ),
    ]
