# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CattleSpecies',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surface_area', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Paintjob',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('due_date', models.DateTimeField(verbose_name='Due date')),
                ('cattle_species', models.ForeignKey(to='paintjobs.CattleSpecies')),
            ],
        ),
    ]
