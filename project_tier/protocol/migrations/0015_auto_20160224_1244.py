# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0014_auto_20160217_1121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='protocolhomepage',
            options={'verbose_name': 'Protocol Landing Page'},
        ),
    ]
