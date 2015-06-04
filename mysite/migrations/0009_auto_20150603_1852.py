# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20150603_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='pic',
            name='finaljudge',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='pic',
            name='sn',
            field=models.CharField(default=b'', max_length=30),
        ),
    ]
