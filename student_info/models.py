# -*- coding: utf-8 -*-
import uuid
from datetime import datetime

from django.db import models
from django.db.models import ManyToManyField, DecimalField, DateTimeField

SEX_CHOICES = (
    ('man', '男'),
    ('woman', '女'),
    ('other', '其他')
)


class BaseModel(models.Model):
    id = models.CharField(db_column='id', primary_key=True, default=uuid.uuid4, editable=False, max_length=36,
                          verbose_name=u'ID')
    desc = models.TextField(db_column="desc", blank=True, null=True, verbose_name=u"说明")
    delflag = models.BooleanField(db_column='delflag', default=False, verbose_name=u'删除标志')
    created = models.DateTimeField(db_column='created', default=datetime.now, blank=True, verbose_name=u'创建时间')
    updated = models.DateTimeField(db_column='updated', auto_now=True, blank=True, verbose_name=u'最后更新时间')
    creator = models.CharField(db_column='creator', max_length=64, blank=True, null=True, verbose_name=u'创建人')
    modifier = models.CharField(db_column='modifier', max_length=64, blank=True, null=True, verbose_name=u'最后更新人')

    def to_dict(self, fields=None, exclude=None):
        data = {}
        for f in self._meta.concrete_fields + self._meta.many_to_many:
            value = f.value_from_object(self)
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, ManyToManyField):
                value = [i.id for i in value] if self.pk else None
            if isinstance(f, DecimalField):
                value = float(value)
            if isinstance(f, DateTimeField):
                value = value.strftime('%Y-%m-%d %H:%M:%S') if value else None
            data[f.name] = value
        return data

    class Meta:
        abstract = True


class User(BaseModel):
    user_name = models.CharField(max_length=64)
    user_password = models.CharField(max_length=64)  # todo md5加密


class Profession(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, null=True, blank=True, verbose_name=u"专业编号")
    name = models.CharField(db_column="name", max_length=64, verbose_name=u"专业名称")


class ClassInfo(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, null=True, blank=True, verbose_name=u"班级编号")
    start_time = models.DateTimeField(verbose_name=u"开班时间")
    profession = models.ForeignKey(Profession)


class Course(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, null=True, blank=True, verbose_name=u"课程编号")
    name = models.CharField(db_column="name", max_length=64, verbose_name=u"课程名称")
    profession = models.ForeignKey(Profession)


class Duty(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, null=True, blank=True, verbose_name=u"职务编号")
    name = models.CharField(db_column="name", max_length=64, verbose_name=u"职务名称")


class Teacher(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, null=True, blank=True, verbose_name=u"教师编号")
    name = models.CharField(db_column="name", max_length=64, verbose_name=u"教师姓名")
    job_title = models.CharField(db_column="title", max_length=64, blank=True, null=True, verbose_name=u"职称")
    duty = models.ForeignKey(Duty)
    course = models.ForeignKey(Course)


class ClassTeacherAttachment(BaseModel):
    class_info = models.ForeignKey(ClassInfo)
    teacher = models.ForeignKey(Teacher)


class Scholarship(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, null=True, blank=True, verbose_name=u"奖学金代码")
    name = models.CharField(db_column="name", max_length=64, verbose_name=u"奖学金名称")
    amount = models.IntegerField(db_column="amount", verbose_name=u"奖学金金额")


class Bursary(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, null=True, blank=True, verbose_name=u"助学金代码")
    name = models.CharField(db_column="name", max_length=64, verbose_name=u"助学金名称")
    amount = models.IntegerField(db_column="amount", verbose_name=u"助学金金额")


class Dorm(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, verbose_name=u"宿舍号")


class Discipline(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, null=True, blank=True, verbose_name=u"惩罚代码")
    discipline_time = models.DateTimeField(db_column="time", verbose_name=u"惩罚时间")


class Activity(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, null=True, blank=True, verbose_name=u"活动编号")
    name = models.CharField(db_column="name", max_length=64, verbose_name=u"活动名称")
    activity_time = models.DateTimeField(db_column="time", verbose_name=u"活动时间")


class Student(BaseModel):
    sn = models.CharField(db_column="sn", max_length=64, verbose_name=u"学号")
    name = models.CharField(db_column="name", max_length=64, verbose_name=u"姓名")
    class_info = models.ForeignKey(ClassInfo)
    profession = models.ForeignKey(Profession)
    punishment = models.ForeignKey(Discipline, null=True, blank=True)
    dorm = models.ForeignKey(Dorm)
    birthday = models.DateTimeField(db_column="birthday", max_length=64, null=True, blank=True, verbose_name=u"出生年月")
    sex = models.CharField(db_column='sex', choices=SEX_CHOICES, default='man', verbose_name=u"性别", max_length=16)
    id_card = models.CharField(db_column="id_card", max_length=64, null=True, blank=True, verbose_name=u"证件号")
    politics = models.CharField(db_column="politics", max_length=64, null=True, blank=True, verbose_name=u"政治面貌")
    hometown = models.CharField(db_column="hometown", max_length=64, null=True, blank=True, verbose_name=u"籍贯")
    country = models.CharField(db_column="country", max_length=64, null=True, blank=True, verbose_name=u"国籍")
    nation = models.CharField(db_column="nation", max_length=64, null=True, blank=True, verbose_name=u"民族")
    phone = models.CharField(db_column="phone", max_length=64, null=True, blank=True, verbose_name=u"联系电话")
    father_phone = models.CharField(db_column="father_phone", max_length=64, null=True, blank=True,
                                    verbose_name=u"父亲联系电话")
    mother_phone = models.CharField(db_column="mother_phone", max_length=64, null=True, blank=True,
                                    verbose_name=u"母亲联系方式")
    address = models.CharField(db_column="address", max_length=64, null=True, blank=True, verbose_name=u"家庭住址")
    qq = models.CharField(db_column="qq", null=True, max_length=64, blank=True, verbose_name=u"QQ")
    email = models.CharField(db_column="email", max_length=64, null=True, blank=True, verbose_name=u"email")
    is_focus = models.BooleanField(db_column="is_focus", default=False, verbose_name=u"是否为重点关注学生")
    focus_reason = models.TextField(db_column="focus_reason", null=True, blank=True, verbose_name=u"关注原因")


# 奖学金
class ScholarshipStudentAttachment(BaseModel):
    scholarship = models.ForeignKey(Scholarship)
    student = models.ForeignKey(Student)
    release_time = models.DateTimeField(db_column="release_time", verbose_name=u"发放时间")


class BursaryStudentAttachment(BaseModel):
    bursary = models.ForeignKey(Bursary)
    student = models.ForeignKey(Student)
    release_time = models.DateTimeField(db_column="release_time", verbose_name=u"发放时间")


class StudentActivityAttachment(BaseModel):
    student = models.ForeignKey(Student)
    activity = models.ForeignKey(Activity)


class ChatHistory(BaseModel):
    student = models.ForeignKey(Student)
    chatTime = models.DateTimeField(db_column="chart_time", verbose_name=u"谈话时间")
