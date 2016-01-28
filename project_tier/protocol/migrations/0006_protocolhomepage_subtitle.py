# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0005_auto_20160120_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocolhomepage',
            name='subtitle',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]
