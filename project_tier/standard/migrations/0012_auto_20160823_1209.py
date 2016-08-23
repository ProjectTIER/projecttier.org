# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailcore', '0028_merge'),
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('standard', '0011_protocolpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protocolpage',
            name='page_ptr',
        ),
        migrations.AddField(
            model_name='standardindexpage',
            name='title_suffix',
            field=models.CharField(blank=True, help_text="Additional text to display after the page title e.g. '(Version 3.0)", max_length=255),
        ),
        migrations.DeleteModel(
            name='ProtocolPage',
        ),
    ]
