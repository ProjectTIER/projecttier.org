# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0014_auto_20160827_1110'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personcategory',
            options={'verbose_name': 'People category', 'verbose_name_plural': 'People categories'},
        ),
    ]
