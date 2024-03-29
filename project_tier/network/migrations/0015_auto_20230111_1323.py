# Generated by Django 3.1.14 on 2023-01-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_auto_20220121_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='fellowship_year',
            field=models.IntegerField(blank=True, choices=[(2010, '2010–2011'), (2011, '2011–2012'), (2012, '2012–2013'), (2013, '2013–2014'), (2014, '2014–2015'), (2015, '2015–2016'), (2016, '2016–2017'), (2017, '2017–2018'), (2018, '2018–2019'), (2019, '2019–2020'), (2020, '2020–2021'), (2021, '2021–2022'), (2022, '2022–2023'), (2023, '2023–2024')], null=True),
        ),
    ]
