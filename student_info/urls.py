# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'student_info.views',
    (r'^overview/$', 'overview'),
    (r'^overview/chart/$', 'overview_chart'),

    (r'^$', 'home'),
    (r'^student/$', 'student_list'),
    (r'^student/delete/$', 'student_delete'),
    (r'^student/add/$', 'student_add_page'),
    (r'^student/add/save/$', 'student_add_save'),
    (r'^student/detail/$', 'student_detail'),
    (r'^student/detail/scholarship/$', 'student_detail_scholarship'),
    (r'^student/detail/chat/$', 'student_detail_chat'),

    (r'^teacher/page/$', 'teacher_page'),
    (r'^teacher/$', 'teacher_list'),
    (r'^teacher/add/page/$', 'teacher_add_page'),
    (r'^teacher/add/save/$', 'teacher_add_save'),
    (r'^teacher/delete/$', 'teacher_delete'),

    (r'^class_info/$', 'class_info_list'),
    (r'^class_info/page/$', 'class_page'),

    (r'^scholarship/page/$', 'scholarship_page'),
    (r'^scholarship/$', 'scholarship_list'),
    (r'^scholarship/add/page/$', 'scholarship_add_page'),
    (r'^scholarship/add/save/$', 'scholarship_add_save'),
    (r'^scholarship/delete/$', 'scholarship_delete'),

)
