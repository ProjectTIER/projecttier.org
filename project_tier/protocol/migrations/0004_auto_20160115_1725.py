# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0003_protocolprocesspage_protocolprocesssection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='protocolprocesspage',
            options={'verbose_name': 'Protocol Process Page'},
        ),
    ]
