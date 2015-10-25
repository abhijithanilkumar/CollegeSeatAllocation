# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='alloted',
            field=models.ForeignKey(related_name='profile_allotted', default=1, to='seats.Branch'),
        ),
        migrations.AddField(
            model_name='profile',
            name='alloted_pref',
            field=models.IntegerField(default=0, choices=[(0, 'None'), (1, 'Preference 1'), (2, 'Preference 2'), (3, 'Preference 3')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='pref1',
            field=models.ForeignKey(related_name='profile_pref_1', default=1, to='seats.Branch'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pref2',
            field=models.ForeignKey(related_name='profile_pref_2', default=1, to='seats.Branch'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pref3',
            field=models.ForeignKey(related_name='profile_pref_3', default=1, to='seats.Branch'),
        ),
        migrations.AddField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
