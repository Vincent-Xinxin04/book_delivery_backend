from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.views.decorators.http import require_http_methods
import json
from index.models import *
# Create your views here.
@csrf_exempt
@require_GET
def profile(request):
    if request.body is None:
        return JsonResponse({'msg':'请求体为空'},status=400)
    try:
        content = json.loads(request.body.decode('utf-8'))  #给个学号即可
    except Exception:
        return JsonResponse({'msg':'Json不合法'},status=400)
    try:
        obj = User.objects.filter(student_id=content['username'])
    except Exception:
        return JsonResponse({'msg':'服务器错误'},status=500)
    if len(obj) == 1:
        return JsonResponse({'msg':'用户信息',
                             'username':obj[0].Username,
                             'studentid':obj[0].student_id,
                             'email':obj[0].email,'create_time':obj[0].create_time},
                            status=200)
    else:
        return JsonResponse({'msg':'用户不唯一'},status=400)

@csrf_exempt
@require_http_methods(['PUT'])
def update(request):
    if request.body is None:
        return JsonResponse({'msg':'请求体无效'},status=400)
    try:
        content = json.loads(request.body.decode('utf-8'))
    except Exception:
        return JsonResponse({'msg':'Json不合法'},status=400)
    try:
        obj = User.objects.filter(student_id=content['studentid'])
    except Exception:
        return JsonResponse({'msg':'服务器错误'},status=500)
    if len(obj) == 1:   #学号应该禁止修改?
        username = content['username']
        studentid = content['studentid']
        email = content['email']
        User.objects.filter(student_id=studentid).update(Username=username,email=email)
        return JsonResponse({'msg':'更新成功'},status=200)
    else:
        return JsonResponse({'msg':'用户不唯一'},status=400)

