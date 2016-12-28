from django.http import HttpResponse
from django.shortcuts import render

def hello(request):

    context={}
    context["hello"] = "hello world"
    context["world"] = "hello world"

    return render(request,"helloworld.html",context)