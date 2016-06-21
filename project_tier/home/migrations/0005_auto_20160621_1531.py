# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160621_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='intro',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='tagline',
        ),
        migrations.AddField(
            model_name='homepage',
            name='headline',
            field=models.CharField(help_text='Write a short introductory sentence about Project TIER.', max_length=255, default='Promoting transparency & reproducibility in empirical social science research.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_events_page',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', help_text='Select the main events listing page.', to='wagtailcore.Page', null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_index_page',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', help_text='Choose the most important index page on the site. It will be prominently featured on the home page.', to='wagtailcore.Page', null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_index_page_2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', help_text='Choose an important secondary page to feature.', to='wagtailcore.Page', verbose_name='Secondary featured page', null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='featured_index_page_3',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', help_text='Choose an important secondary page to feature.', to='wagtailcore.Page', verbose_name='Secondary featured page', null=True),
        ),
    ]
