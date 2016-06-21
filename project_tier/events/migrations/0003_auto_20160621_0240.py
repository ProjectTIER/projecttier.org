# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventpage_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventindexpagerelatedlink',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='eventindexpagerelatedlink',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='eventindexpagerelatedlink',
            name='page',
        ),
        migrations.DeleteModel(
            name='EventIndexPageRelatedLink',
        ),
    ]
