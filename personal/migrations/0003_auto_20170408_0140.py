# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 20:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20170401_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('N', 'Not Specific')], default='Not Specific', max_length=20),
        ),
    ]
