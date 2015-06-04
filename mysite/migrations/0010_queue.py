# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20150603_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('sdatetime', models.DateTimeField(default=datetime.datetime.now)),
                ('pic', models.ForeignKey(to='mysite.Pic')),
            ],
        ),
    ]
