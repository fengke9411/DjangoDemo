# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# Create your models here.


# python manage.py makemigrations
# python manage.py migrate

class Test(models.Model):
    name = models.CharField(max_length=20)
    time = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=20)


class Avatar(models.Model):
    avatarToken = models.CharField(max_length=20)  # 头像token
    avatarSource = models.CharField(max_length=30)  # 头像地址

    def __unicode__(self):
        return self.avatarToken


class Skill(models.Model):
    name = models.CharField(max_length=20)
    parentClass = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    startTime = models.CharField(max_length=20)
    endTime = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    responsibility = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class WorkExperience(models.Model):
    startTime = models.CharField(max_length=20)
    endTime = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    jobDescription = models.CharField(max_length=20)

    def __unicode__(self):
        return self.company


class User(models.Model):
    username = models.CharField(max_length=20)  # 用户名
    password = models.CharField(max_length=30)  # 密码
    nickname = models.CharField(max_length=20)  # 昵称
    loginTime = models.CharField(max_length=30)  # 登录时间
    avatarToken = models.ForeignKey(Avatar)  # 一对多
    loginIp = models.CharField(max_length=20)  # ip
    loginAddress = models.CharField(max_length=20)  # 登录地点
    skillTree = models.ManyToManyField(Skill)  # 多对多  技能表
    projects = models.ForeignKey(Project)  # 一对多 项目表
    integral = models.IntegerField()  # 用户积分
    signature = models.CharField(max_length=50)  # 签名
    birthday = models.CharField(max_length=20)  # 生日
    mobile = models.CharField(max_length=20)  # 手机号
    email = models.CharField(max_length=20)  # 邮箱
    location = models.CharField(max_length=20)  # 住址
    workExperience = models.ForeignKey(WorkExperience)  # 工作经历

    def __unicode__(self):
        return self.username




class Article(models.Model):
    title = models.CharField(max_length=100)
    publishTime = models.CharField(max_length=30)
    author = models.ForeignKey(User)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    describe = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title
