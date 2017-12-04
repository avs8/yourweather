# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherdaily', '0003_auto_20171130_1600'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Weather',
            new_name='Users',
        ),
    ]
