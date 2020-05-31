# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_phone',
            field=models.CharField(max_length=64, null=True, verbose_name='\u7236\u4eb2\u8054\u7cfb\u7535\u8bdd', db_column=b'father_phone', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mother_phone',
            field=models.CharField(max_length=64, null=True, verbose_name='\u6bcd\u4eb2\u8054\u7cfb\u65b9\u5f0f', db_column=b'mother_phone', blank=True),
        ),
    ]
