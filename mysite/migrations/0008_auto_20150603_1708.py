# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20150603_1636'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_pic_rel',
            old_name='picid',
            new_name='pic',
        ),
        migrations.RenameField(
            model_name='user_pic_rel',
            old_name='uid',
            new_name='usr',
        ),
    ]
