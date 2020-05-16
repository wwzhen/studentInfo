# -*- coding: utf-8 -*-

# import from apps here


# import from lib
# ===============================================================================
# from django.contrib import admin
# from apps.__.models import aaaa
#
# admin.site.register(aaaa)
# ===============================================================================
from django.contrib import admin

from student_info.models import User, Profession, ClassInfo, Course, Duty, Teacher, ClassTeacherAttachment, Scholarship, \
    Bursary, Dorm, Student, ScholarshipStudentAttachment

admin.site.register(
    [User, Profession, ClassInfo, Course, Duty, Teacher, ClassTeacherAttachment, Scholarship, Bursary, Dorm, Student,
     ScholarshipStudentAttachment])
