# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import json

def convert_to_streamfield(apps, schema_editor):
    StandardPage = apps.get_model("home", "StandardPage")
    for page in StandardPage.objects.all():
        page.body = json.dumps([{ 'type': 'rich_text', 'value': page.body }])
        page.save()


def convert_to_richtext(apps, schema_editor):
    StandardPage = apps.get_model("home", "StandardPage")
    for page in StandardPage.objects.all():
        if page.body.raw_text is None:
            raw_text = ''.join([
                child.value.source for child in page.body
                if child.block_type == 'rich_text'
            ])
            page.body = raw_text
            page.save()

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_remove_newsarticle_date'),
    ]

    operations = [
        migrations.RunPython(
            convert_to_streamfield,
            convert_to_richtext,
        ),
    ]
