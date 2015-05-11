# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.FileField(upload_to=b'pic/%Y/%m/%d')),
            ],
        ),
        migrations.AlterField(
            model_name='pic',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 5, 11, 3, 17, 20, 717522)),
        ),
    ]
