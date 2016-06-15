# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_auto_20160615_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='school',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='testimony',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonial',
            name='year',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
