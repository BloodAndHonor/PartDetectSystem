# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(default=datetime.datetime(2015, 5, 6, 16, 12, 58, 901425))),
                ('ratesum', models.IntegerField(default=0)),
                ('qualifiedsum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('last_logtime', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='User_Pic_Rel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('picid', models.IntegerField(default=0, db_index=True)),
                ('uid', models.IntegerField(default=0, db_index=True)),
                ('qualified', models.BooleanField(default=False)),
            ],
        ),
    ]
