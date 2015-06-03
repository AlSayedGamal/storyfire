# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20150603_0701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stakeholder',
            old_name='Stakeholder_name',
            new_name='stakeholder_name',
        ),
    ]
