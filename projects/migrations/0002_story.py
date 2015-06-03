# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('story_name', models.CharField(max_length=200)),
                ('story_goal', models.CharField(max_length=200)),
                ('story_function', models.CharField(max_length=200)),
                ('sprint', models.ForeignKey(to='projects.Sprint')),
                ('stakeholder', models.ForeignKey(to='projects.Stakeholder')),
            ],
        ),
    ]
