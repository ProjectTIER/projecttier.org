# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20160621_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fellowshipsindexpage',
            name='related_person_index_page',
            field=models.ForeignKey(help_text='Select the person index page to pull the list of fellows from.', to='wagtailcore.Page', on_delete=django.db.models.deletion.PROTECT, related_name='+'),
        ),
    ]
