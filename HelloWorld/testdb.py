# -*- coding: utf-8 -*-
from django.http import HttpResponse

from TestModel.models import Test
import time
from django.views import csrf

def testdb(request):
    request.encoding="utf-8"

    ctx = {}
    ctx.update(csrf(request))

    for var in request.GET:
        print "request = " + request.GET[var].encode("utf-8")

    return HttpResponse("<p>数据库添加成功</p>")

def postTest(request):
    for cookie in request.COOKIES:
        print "cookie "+cookie+"value "+request.COOKIES.get(cookie)
    for key in request.POST:
        print "key  "+request.POST.get(key)
    return HttpResponse("post请求")