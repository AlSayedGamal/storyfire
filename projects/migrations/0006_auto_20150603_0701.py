# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
