# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20160622_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventpage',
            name='department',
        ),
        migrations.RemoveField(
            model_name='eventpage',
            name='university',
        ),
        migrations.AddField(
            model_name='eventpage',
            name='description_past',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='The description written as though in the past'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='date_from',
            field=models.DateField(verbose_name='Start date', help_text='Required for us to know if the event is in the future or past'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='The description written as though in the future'),
        ),
    ]
