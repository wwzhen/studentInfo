# -*- coding: utf-8 -*-
import json

import constant
from common.mymako import render_mako_context, render_json
from student_info.models import Student, Profession, ClassInfo, Dorm


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
    student_models = Student.objects.filter(delflag=False)
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
    countries = constant.country
    nations = constant.nations
    profession_models = Profession.objects.filter(delflag=False)
    professions = map(lambda x: x.to_dict(), profession_models)
    class_models = ClassInfo.objects.filter(delflag=False)
    classes = map(lambda x: x.to_dict(), class_models)
    dorm_models = Dorm.objects.filter(delflag=False)
    dorms = map(lambda x: x.to_dict(), dorm_models)
    return render_mako_context(request, '/home_application/student_add.html',
                               {"countries": countries,
                                "nations": nations,
                                "professions": professions,
                                "classes": classes,
                                "dorms": dorms
                                })


def student_add_save(request):
    params = request.POST
    model_dict = dict()
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
    model_dict['birthday'] = params.get('birthday')
    model_dict['id_card'] = params.get("idCard")
    model_dict['phone'] = params.get("phone")
    model_dict['politics'] = params.get("politics")
    model_dict['country'] = params.get("country")
    model_dict['nation'] = params.get("nation")
    model_dict['hometown'] = params.get("hometown")
    model_dict['emergency_phone'] = params.get("emergencyPhone")
    model_dict['address'] = params.get("address")
    model_dict['qq'] = params.get("qq")
    model_dict['email'] = params.get('email')
    student_info_model = Student(**model_dict)
    student_info_model.save()
    return render_json({"result": True})