# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'student_info.views',
    (r'^$', 'home'),
    (r'^student/$', 'student_list'),
    (r'^student/delete/$', 'student_delete'),
    (r'^student/add/$', 'student_add_page'),
    (r'^student/add/save/$', 'student_add_save'),
)
