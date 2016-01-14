# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_testpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testpage',
            name='template_path',
            field=models.CharField(help_text='Use any filename in home/template/home/', max_length=255),
        ),
    ]
