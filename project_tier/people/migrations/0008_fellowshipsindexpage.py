# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('people', '0007_fellowpersonpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='FellowshipsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, primary_key=True, to='wagtailcore.Page')),
                ('related_person_index_page', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, help_text='Select the person index page to pull the list of fellows from.', blank=True, null=True, related_name='+', to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
