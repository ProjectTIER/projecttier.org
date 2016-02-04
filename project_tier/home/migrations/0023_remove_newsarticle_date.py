# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_newsarticle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsarticle',
            name='date',
        ),
    ]
