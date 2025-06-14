import json
import os
from http.client import responses

from django.contrib.admindocs.utils import ROLES
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt,csrf_protect

from algorithm.crypt_jwt import generate_login_token
from index.models import *
from algorithm import crypt_jwt
from index.models import Role

def index(request):
    Role.objects.create(Role_ID=1,Role_name='monitor')
    Role.objects.create(Role_ID=2,Role_name='common_user')
    Role.objects.create(Role_ID=3,Role_name='volunteer')
    return

@csrf_exempt
@require_POST
def login(request):
    # print(request.body)
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
    try:
        obj = User.objects.filter(student_id=content['studentid'])
    except Exception:
        return JsonResponse({'msg':'服务器错误'}, status=400)
    if len(obj) == 1:
        token = generate_login_token(obj[0].student_id,obj[0].Username,crypt_jwt.secert_key)
        if crypt_jwt.verify_password(content['password'], obj[0].password):
            role = Role.objects.get(Role_ID=User_Role.objects.get(User_ID = obj[0].UserID).Role_ID_id).Role_ID
            response.content = JsonResponse({
                'role':role,
                'userdata': {
                    'userid': obj[0].UserID,
                    'username': obj[0].Username,
                    'studentid': obj[0].student_id,
                    'email': obj[0].email
                },
                'token':token,
                'msg':'登录成功',
                })
            response.status_code = 200
            return response
        else :
            response.status_code = 400
            response.content = JsonResponse({'msg': '密码错误'})
            return response
    else:
        response.status_code = 400
        response.content = JsonResponse({'msg': '用户不存在'})
        return response

@csrf_exempt
@require_POST
def signup(request):
    if not request.body:
        return JsonResponse({'msg': '请求为空'}, status=400)
    try:
        content = json.loads(request.body.decode('utf-8'))
        print(content)
    except Exception:
        return JsonResponse({'msg': '请求体不是合法Json'}, status=500)
    if content['studentid'] is None : return JsonResponse({'msg':'学号为空'}, status=400)
    if content['password'] is None : return JsonResponse({'msg':'密码为空'}, status=400)
    try:
        obj = User.objects.filter(student_id=content['studentid'])
    except Exception:
        return JsonResponse({'msg':'服务器出现错误'}, status=400)
    if len(obj) == 0:
        User.objects.create(Username= content['username'], password=crypt_jwt.encrypt_password(content['password']),student_id=content['studentid'],email=content['email'])
        ID = User.objects.get(student_id=content['studentid']).UserID
        # print(ID)
        User_Role.objects.create(User_ID_id=ID,Role_ID_id=2)
        return JsonResponse({'msg':'注册成功'}, status=200)
    else:
        return JsonResponse({'msg':'用户已存在'},status=400)

