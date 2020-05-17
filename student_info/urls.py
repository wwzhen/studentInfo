# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'student_info.views',
    (r'^overview/$', 'overview'),
    (r'^overview/student/chart/$', 'overview_student_chart'),

    (r'^$', 'home'),
    (r'^student/$', 'student_list'),
    (r'^student/delete/$', 'student_delete'),
    (r'^student/add/$', 'student_add_page'),
    (r'^student/add/save/$', 'student_add_save'),

    (r'^teacher/page/$', 'teacher_page'),
    (r'^teacher/$', 'teacher_list'),
    (r'^teacher/add/page/$', 'teacher_add_page'),
    (r'^teacher/add/save/$', 'teacher_add_save'),
    (r'^teacher/delete/$', 'teacher_delete'),

    (r'^class_info/$', 'class_info_list'),
    (r'^class_info/page/$', 'class_page'),
)
