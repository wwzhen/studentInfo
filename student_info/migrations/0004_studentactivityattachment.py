# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('student_info', '0003_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentActivityAttachment',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('activity', models.ForeignKey(to='student_info.Activity')),
                ('student', models.ForeignKey(to='student_info.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
