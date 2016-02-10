# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0012_auto_20160204_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentpage',
            name='type',
            field=models.CharField(default='folder', max_length=255, choices=[('folder', 'Folder'), ('file', 'Text'), ('data', 'Data'), ('multiple', 'Multiple')]),
        ),
    ]
