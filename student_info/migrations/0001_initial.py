# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bursary',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('sn', models.CharField(max_length=64, null=True, verbose_name='\u52a9\u5b66\u91d1\u4ee3\u7801', db_column=b'sn', blank=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u52a9\u5b66\u91d1\u540d\u79f0', db_column=b'name')),
                ('amount', models.IntegerField(verbose_name='\u52a9\u5b66\u91d1\u91d1\u989d', db_column=b'amount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BursaryStudentAttachment',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('release_time', models.DateTimeField(verbose_name='\u53d1\u653e\u65f6\u95f4', db_column=b'release_time')),
                ('bursary', models.ForeignKey(to='student_info.Bursary')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('sn', models.CharField(max_length=64, null=True, verbose_name='\u73ed\u7ea7\u7f16\u53f7', db_column=b'sn', blank=True)),
                ('start_time', models.DateTimeField(verbose_name='\u5f00\u73ed\u65f6\u95f4')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassTeacherAttachment',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('class_info', models.ForeignKey(to='student_info.ClassInfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('sn', models.CharField(max_length=64, null=True, verbose_name='\u8bfe\u7a0b\u7f16\u53f7', db_column=b'sn', blank=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u8bfe\u7a0b\u540d\u79f0', db_column=b'name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dorm',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('sn', models.CharField(max_length=64, verbose_name='\u5bbf\u820d\u53f7', db_column=b'sn')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('sn', models.CharField(max_length=64, null=True, verbose_name='\u804c\u52a1\u7f16\u53f7', db_column=b'sn', blank=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u804c\u52a1\u540d\u79f0', db_column=b'name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('sn', models.CharField(max_length=64, null=True, verbose_name='\u4e13\u4e1a\u7f16\u53f7', db_column=b'sn', blank=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u4e13\u4e1a\u540d\u79f0', db_column=b'name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('sn', models.CharField(max_length=64, null=True, verbose_name='\u5956\u5b66\u91d1\u4ee3\u7801', db_column=b'sn', blank=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u5956\u5b66\u91d1\u540d\u79f0', db_column=b'name')),
                ('amount', models.IntegerField(verbose_name='\u5956\u5b66\u91d1\u91d1\u989d', db_column=b'amount')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScholarshipStudentAttachment',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('release_time', models.DateTimeField(verbose_name='\u53d1\u653e\u65f6\u95f4', db_column=b'release_time')),
                ('scholarship', models.ForeignKey(to='student_info.Scholarship')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('sn', models.CharField(max_length=64, verbose_name='\u5b66\u53f7', db_column=b'sn')),
                ('name', models.CharField(max_length=64, verbose_name='\u59d3\u540d', db_column=b'name')),
                ('birthday', models.DateTimeField(max_length=64, null=True, verbose_name='\u51fa\u751f\u5e74\u6708', db_column=b'birthday', blank=True)),
                ('id_card', models.CharField(max_length=64, null=True, verbose_name='\u8bc1\u4ef6\u53f7', db_column=b'id_card', blank=True)),
                ('politics', models.CharField(max_length=64, null=True, verbose_name='\u653f\u6cbb\u9762\u8c8c', db_column=b'politics', blank=True)),
                ('hometown', models.CharField(max_length=64, null=True, verbose_name='\u7c4d\u8d2f', db_column=b'hometown', blank=True)),
                ('country', models.CharField(max_length=64, null=True, verbose_name='\u56fd\u7c4d', db_column=b'country', blank=True)),
                ('nation', models.CharField(max_length=64, null=True, verbose_name='\u6c11\u65cf', db_column=b'nation', blank=True)),
                ('phone', models.CharField(max_length=64, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd', db_column=b'phone', blank=True)),
                ('emergency_phone', models.CharField(max_length=64, null=True, verbose_name='\u7d27\u6025\u8054\u7cfb\u4eba', db_column=b'emergency_phone', blank=True)),
                ('address', models.CharField(max_length=64, null=True, verbose_name='\u5bb6\u5ead\u4f4f\u5740', db_column=b'address', blank=True)),
                ('qq', models.CharField(max_length=64, null=True, verbose_name='QQ', db_column=b'qq', blank=True)),
                ('email', models.CharField(max_length=64, null=True, verbose_name='email', db_column=b'email', blank=True)),
                ('class_info', models.ForeignKey(to='student_info.ClassInfo')),
                ('dorm', models.ForeignKey(to='student_info.Dorm')),
                ('profession', models.ForeignKey(to='student_info.Profession')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.CharField(primary_key=True, db_column=b'id', default=uuid.uuid4, serialize=False, editable=False, max_length=36, verbose_name='ID')),
                ('desc', models.TextField(null=True, verbose_name='\u8bf4\u660e', db_column=b'desc', blank=True)),
                ('delflag', models.BooleanField(default=False, verbose_name='\u5220\u9664\u6807\u5fd7', db_column=b'delflag')),
                ('created', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u521b\u5efa\u65f6\u95f4', db_column=b'created', blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='\u6700\u540e\u66f4\u65b0\u65f6\u95f4', db_column=b'updated')),
                ('creator', models.CharField(max_length=64, null=True, verbose_name='\u521b\u5efa\u4eba', db_column=b'creator', blank=True)),
                ('modifier', models.CharField(max_length=64, null=True, verbose_name='\u6700\u540e\u66f4\u65b0\u4eba', db_column=b'modifier', blank=True)),
                ('sn', models.CharField(max_length=64, null=True, verbose_name='\u6559\u5e08\u7f16\u53f7', db_column=b'sn', blank=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u6559\u5e08\u59d3\u540d', db_column=b'name')),
                ('job_title', models.CharField(max_length=64, null=True, verbose_name='\u804c\u79f0', db_column=b'title', blank=True)),
                ('course', models.ForeignKey(to='student_info.Course')),
                ('duty', models.ForeignKey(to='student_info.Duty')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='scholarshipstudentattachment',
            name='student',
            field=models.ForeignKey(to='student_info.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='profession',
            field=models.ForeignKey(to='student_info.Profession'),
        ),
        migrations.AddField(
            model_name='classteacherattachment',
            name='teacher',
            field=models.ForeignKey(to='student_info.Teacher'),
        ),
        migrations.AddField(
            model_name='classinfo',
            name='profession',
            field=models.ForeignKey(to='student_info.Profession'),
        ),
        migrations.AddField(
            model_name='bursarystudentattachment',
            name='student',
            field=models.ForeignKey(to='student_info.Student'),
        ),
    ]
