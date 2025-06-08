from http.client import responses
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    response = HttpResponse('528图书派送系统后端项目')
    print('hello')
    return response