# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20151025_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='alloted',
            new_name='allotted',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='alloted_pref',
            new_name='allotted_pref',
        ),
    ]
