# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_auto_20150603_1629'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='user_pic_rel',
            name='picid',
            field=models.ForeignKey(to='mysite.Pic'),
        ),
        migrations.AlterField(
            model_name='user_pic_rel',
            name='uid',
            field=models.ForeignKey(to='mysite.User'),
        ),
    ]
