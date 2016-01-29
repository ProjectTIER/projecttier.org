# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0006_protocolhomepage_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolhomepage',
            name='subtitle',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
