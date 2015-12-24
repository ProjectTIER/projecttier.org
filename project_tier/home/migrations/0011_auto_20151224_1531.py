# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20151224_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='personpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='PersonPageRelatedLink',
        ),
    ]
