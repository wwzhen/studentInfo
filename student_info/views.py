# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.db.models import Q

import constant
from common.mymako import render_mako_context, render_json
from student_info.models import Student, Profession, ClassInfo, Dorm, Teacher, Duty, Course, StudentActivityAttachment, \
    Activity, Discipline, Scholarship


def overview(request):
    return render_mako_context(request, '/home_application/overview.html')


def overview_chart(request):
    data = dict()
    student_models = Student.objects.filter(delflag=False)
    data['student_counts'] = student_models.count()
    man_count = 0
    woman_count = 0
    dang_count = 0
    tuan_count = 0
    qun_count = 0
    china_count = 0
    out_count = 0

    for student in student_models:
        if student.sex == 'man':
            man_count += 1
        else:
            woman_count += 1
        if student.politics == u'党员':
            dang_count += 1
        elif student.politics == u"团员":
            tuan_count += 1
        else:
            qun_count += 1
        if student.country == u"中国":
            china_count += 1
        else:
            out_count += 1
    data['student_sex_chart'] = [
        {
            'value': man_count,
            'category': u'男'
        },
        {
            'value': woman_count,
            'category': u'女'
        }
    ]
    data['student_politics_chart'] = [dang_count, tuan_count, qun_count]
    data['student_country_chart'] = [
        {
            'value': china_count,
            'name': u'中国'
        },
        {
            'value': out_count,
            'name': u'留学生'
        }
    ]
    teacher_models = Teacher.objects.filter(delflag=False)
    data['teacher_counts'] = teacher_models.count()
    data['course_counts'] = Course.objects.filter(delflag=False).count()
    data['class_counts'] = ClassInfo.objects.filter(delflag=False).count()
    return render_json(data)


def home(request):
    """
    首页
    """
    countries = constant.country
    nations = constant.nations
    profession_models = Profession.objects.filter(delflag=False)
    professions = map(lambda x: x.to_dict(), profession_models)
    class_models = ClassInfo.objects.filter(delflag=False)
    classes = map(lambda x: x.to_dict(), class_models)
    dorm_models = Dorm.objects.filter(delflag=False)
    dorms = map(lambda x: x.to_dict(), dorm_models)
    return render_mako_context(request, '/home_application/index.html',
                               {"countries": countries,
                                "nations": nations,
                                "professions": professions,
                                "classes": classes,
                                "dorms": dorms
                                })


def student_list(request):
    """
    学生信息列表
    :param request:
    :return:
    """
    params = request.POST
    q_query = Q(delflag=False)
    name = params.get("name")
    if name:
        q_query = q_query & Q(name__contains=name)
    sn = params.get("sn")
    if sn:
        q_query = q_query & Q(sn__contains=sn)
    class_id = params.get("class_id")
    if class_id:
        q_query = q_query & Q(class_id=class_id)
    profession_id = params.get("profession_id")
    if profession_id:
        q_query = q_query & Q(profession_id=profession_id)
    sex = params.get('sex')
    if sex:
        q_query = q_query & Q(sex=sex)
    student_models = Student.objects.filter(q_query)
    students = list()
    for student in student_models:
        student_dict = student.to_dict()
        student_dict['profession_name'] = student.profession.name
        student_dict['class_name'] = student.class_info.sn
        student_dict['dorm_sn'] = student.dorm.sn
        students.append(student_dict)
    return render_json(json.dumps(students))


def student_detail(request):
    """
    学生信息详情
    :param request:
    :return:
    """
    student_id = request.GET.get('id')
    if student_id:
        student_model = Student.objects.get(id=student_id)
        student_dict = student_model.to_dict()
        student_dict['class_name'] = student_model.class_info.sn
        student_dict['profession_name'] = student_model.profession.name
        student_dict['dorm_sn'] = student_model.dorm.sn
        student_activities_models = StudentActivityAttachment.objects.filter(delflag=False, student_id=student_id)
        student_activities = list()
        for s in student_activities_models:
            student_activities.append(s.activity.name)
        student_dict['activities'] = student_activities
        return render_mako_context(request, "/home_application/detail.html", {"student": student_dict})
    return render_mako_context(request, "/home_application/detail.html")


def student_delete(request):
    """
    学生信息删除
    :param request:
    :return:
    """
    student_id = request.POST.get("id")
    student_model = Student.objects.get(delflag=False, id=student_id)
    student_model.delflag = True
    student_model.save()
    return render_json({"result": True})


def student_add_page(request):
    if 'id' in request.GET:
        student_id = request.GET.get('id')
    else:
        student_id = None
    if student_id:
        student_model = Student.objects.get(id=student_id)
        student_info = student_model.to_dict()
        countries = constant.country
        nations = constant.nations
        profession_models = Profession.objects.filter(delflag=False)
        professions = map(lambda x: x.to_dict(), profession_models)
        class_models = ClassInfo.objects.filter(delflag=False)
        classes = map(lambda x: x.to_dict(), class_models)
        dorm_models = Dorm.objects.filter(delflag=False)
        dorms = map(lambda x: x.to_dict(), dorm_models)
        activity_models = Activity.objects.filter(delflag=False)
        activities = map(lambda x: x.to_dict(), activity_models)
        discipline_models = Discipline.objects.filter(delflag=False)
        disciplines = map(lambda x: x.to_dict(), discipline_models)
        student_info['birthday'] = student_info['birthday'][0:10]
        return render_mako_context(request, '/home_application/student_add.html',
                                   {"countries": countries,
                                    "nations": nations,
                                    "professions": professions,
                                    "classes": classes,
                                    "dorms": dorms,
                                    "activities": activities,
                                    "disciplines": disciplines,
                                    "student_info": student_info})

    countries = constant.country
    nations = constant.nations
    profession_models = Profession.objects.filter(delflag=False)
    professions = map(lambda x: x.to_dict(), profession_models)
    class_models = ClassInfo.objects.filter(delflag=False)
    classes = map(lambda x: x.to_dict(), class_models)
    dorm_models = Dorm.objects.filter(delflag=False)
    dorms = map(lambda x: x.to_dict(), dorm_models)
    activity_models = Activity.objects.filter(delflag=False)
    activities = map(lambda x: x.to_dict(), activity_models)
    discipline_models = Discipline.objects.filter(delflag=False)
    disciplines = map(lambda x: x.to_dict(), discipline_models)
    return render_mako_context(request, '/home_application/student_add.html',
                               {"countries": countries,
                                "nations": nations,
                                "professions": professions,
                                "classes": classes,
                                "dorms": dorms,
                                "activities": activities,
                                "disciplines": disciplines,
                                })


def student_add_save(request):
    params = request.POST
    model_dict = dict()
    student_id = params.get('id')
    model_dict['name'] = params.get("name")
    model_dict['sn'] = params.get("sn")
    model_dict['sex'] = params.get("sex")
    class_info_id = params.get("classInfo")
    model_dict['class_info'] = None
    model_dict['profession'] = None
    model_dict['dorm'] = None
    if class_info_id:
        model_dict['class_info'] = ClassInfo.objects.get(id=class_info_id)
    profession_id = params.get("profession")
    if profession_id:
        model_dict['profession'] = Profession.objects.get(id=profession_id)
    dorm_id = params.get("dorm")
    if dorm_id:
        model_dict['dorm'] = Dorm.objects.get(id=dorm_id)
    model_dict['birthday'] = datetime.strptime(params.get('birthday'), '%Y-%m-%d')
    model_dict['phone'] = params.get("phone")
    model_dict['politics'] = params.get("politics")
    model_dict['country'] = params.get("country")
    model_dict['nation'] = params.get("nation")
    model_dict['hometown'] = params.get("hometown")
    model_dict['father_phone'] = params.get("father_phone")
    model_dict['mother_phone'] = params.get("mother_phone")
    model_dict['address'] = params.get("address")
    model_dict['id_card'] = params.get("id_card")
    model_dict['qq'] = params.get("qq")
    model_dict['email'] = params.get('email')
    if student_id:
        student_info_model = Student.objects.filter(id=student_id)
        student_info_model.update(**model_dict)
    else:
        student_info_model = Student(**model_dict)
        student_info_model.save()
    return render_json({"result": True})


def teacher_page(request):
    return render_mako_context(request, '/home_application/teacher.html')


def teacher_list(request):
    teacher_models = Teacher.objects.filter(delflag=False)
    teachers = list()
    for teacher_model in teacher_models:
        teacher_dict = teacher_model.to_dict()
        teacher_dict["duty_name"] = teacher_model.duty.name
        teacher_dict["course_name"] = teacher_model.course.name
        teachers.append(teacher_dict)
    return render_json(json.dumps(teachers))


def teacher_add_page(request):
    duty_models = Duty.objects.filter(delflag=False)
    course_models = Course.objects.filter(delflag=False)
    duties = map(lambda x: x.to_dict(), duty_models)
    courses = map(lambda x: x.to_dict(), course_models)
    return render_mako_context(request, '/home_application/teacher_add.html',
                               {"duties": duties,
                                "courses": courses})


def teacher_add_save(request):
    params = request.POST
    model_dict = dict()
    model_dict['name'] = params.get("name")
    model_dict['sn'] = params.get("sn")
    model_dict['job_title'] = params.get("jobTitle")
    duty_id = params.get("duty")
    if duty_id:
        model_dict['duty'] = Duty.objects.get(id=duty_id)
    course_id = params.get("course")
    if course_id:
        model_dict['course'] = Course.objects.get(id=course_id)
    teacher_model = Teacher(**model_dict)
    teacher_model.save()
    return render_json({"result": True})


def teacher_delete(request):
    teacher_id = request.POST.get('id')
    teacher_model = Teacher.objects.get(id=teacher_id)
    teacher_model.delflag = True
    teacher_model.save()
    return render_json({"result": True})


def class_page(request):
    return render_mako_context(request, "/home_application/class_info.html")


def class_info_list(request):
    class_models = ClassInfo.objects.filter(delflag=False)
    classes = list()
    for class_model in class_models:
        class_info_dict = class_model.to_dict()
        class_info_dict['profession_name'] = class_model.profession.name
        classes.append(class_info_dict)
    return render_json(json.dumps(classes))


def scholarship_page(request):
    return render_mako_context(request, "/home_application/scholarship.html")


def scholarship_list(request):
    scholarship_models = Scholarship.objects.filter(delflag=False)
    scholarships = list()
    for scholarship in scholarship_models:
        teacher_dict = scholarship.to_dict()
        scholarships.append(teacher_dict)
    return render_json(json.dumps(scholarships))
