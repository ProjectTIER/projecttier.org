# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0011_auto_20160621_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fellowpersonpage',
            name='fellowship_year',
            field=models.IntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)], default=2016),
        ),
    ]
