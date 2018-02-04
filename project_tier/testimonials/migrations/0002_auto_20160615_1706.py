# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonialpagerelationship',
            name='page',
        ),
        migrations.AddField(
            model_name='testimonial',
            name='index_page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_testimonials', default='', to='testimonials.TestimonialIndexPage'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TestimonialPageRelationship',
        ),
    ]
