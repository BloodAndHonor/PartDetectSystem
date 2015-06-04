# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20150511_0401'),
    ]

    operations = [
        migrations.CreateModel(
            name='DtVar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=10, blank=True)),
                ('val', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.RenameField(
            model_name='pic',
            old_name='qualifiedsum',
            new_name='unqualifiedsum',
        ),
        migrations.RenameField(
            model_name='pic',
            old_name='ratesum',
            new_name='votesum',
        ),
        migrations.RenameField(
            model_name='user_pic_rel',
            old_name='qualified',
            new_name='unqualified',
        ),
        migrations.AddField(
            model_name='pic',
            name='finished',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='pic',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, db_index=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_logtime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
