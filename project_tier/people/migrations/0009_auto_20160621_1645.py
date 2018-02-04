# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_fellowshipsindexpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fellowshipsindexpage',
            name='related_person_index_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default='', to='wagtailcore.Page', help_text='Select the person index page to pull the list of fellows from.', related_name='+'),
            preserve_default=False,
        ),
    ]
