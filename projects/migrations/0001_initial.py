# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_name', models.CharField(max_length=200)),
                ('customer_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sprint_description', models.TextField(verbose_name=b'')),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Stakeholder_name', models.CharField(max_length=100)),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
        ),
    ]
