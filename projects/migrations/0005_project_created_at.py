# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_remove_project_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 4, 0, 32, 941849, tzinfo=utc)),
        ),
    ]
