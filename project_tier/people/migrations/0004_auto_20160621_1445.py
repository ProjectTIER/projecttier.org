# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_personindexpage_listing_abstract'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personpage',
            old_name='academic_job_title',
            new_name='academic_title',
        ),
    ]
