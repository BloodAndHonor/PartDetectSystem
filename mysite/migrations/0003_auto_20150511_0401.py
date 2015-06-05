# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20150511_0317'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='pic',
            name='docfile',
            field=models.FileField(default=b'settings.MEDIA_ROOT/anonymous.jpg', upload_to=b'pic/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='pic',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='user_pic_rel',
            name='qualified',
            field=models.BooleanField(default=True),
        ),
    ]
