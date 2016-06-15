# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_auto_20160615_1706'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='testimonial',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True, editable=False),
        ),
    ]
