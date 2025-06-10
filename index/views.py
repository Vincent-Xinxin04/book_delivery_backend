import json
from http.client import responses

from django.contrib.admindocs.utils import ROLES
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt,csrf_protect

from index.models import User
from algorithm import test
from index.models import Role

def index(request):
    response = HttpResponse('528图书派送系统后端项目')
    response.status_code = 200
    return response

@csrf_exempt
@require_POST
def login(request):
    if not request.body:
        return JsonResponse({'msg': '请求体为空'}, status=400)
    try:
        content = json.loads(request.body.decode('utf-8'))
    except Exception:
        return JsonResponse({'msg': '请求体不是合法JSON'}, status=400)
    response = HttpResponse()
    if content['studentid'] is None :
        response.content = JsonResponse({'msg':'学号不存在'})
        response.status_code = 400
        return response
    if content['password'] is None :
        response.content = JsonResponse({'msg':'密码不存在'})
        response.status_code = 400
        return response
    obj = User.objects.filter(student_id=content['studentid'])
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