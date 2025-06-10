import json
from http.client import responses

from django.contrib.admindocs.utils import ROLES
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from index.models import User
from algorithm import test
from index.models import Role

# Create your views here.


def index(request):
    response = HttpResponse('528图书派送系统后端项目')
    response.status_code = 200
    return response

@require_POST
def login(request):
    content = json.loads(request.body)
    response = HttpResponse()
    if content['studentid'] is None :
        response.content = JsonResponse({'msg':'学号不存在'})
        response.status_code = 400
        return response
    if content['password'] is None :
        response.content = JsonResponse({'msg':'密码不存在'})
        response.status_code = 400
        return response
    obj = User.objects.filter(username=content['username'])
    if len(obj) == 1:
        if content['password'] == obj[0].password :
            response.content = JsonResponse({'msg':'登录成功'})
            response.status_code = 200
            return response
        else :
            response.status_code = 400
            response.content = JsonResponse({'msg': '密码错误'})
            return response
    else:
        response.content = JsonResponse({'msg': '用户不存在'})
        response.status_code = 200
        return response

def signup(request):
    return