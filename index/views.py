from http.client import responses
from django.http import HttpResponse
from django.shortcuts import render
from algorithm import test
# Create your views here.


def index(request):
    response = HttpResponse('528图书派送系统后端项目')
    a = 1
    b = 2
    print(test.add(a,b))
    return response