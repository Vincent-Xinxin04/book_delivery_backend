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
    try:
        obj = User.objects.filter(student_id=request.GET['studentid'])
        print(obj)
    except Exception:
        return JsonResponse({'msg':'服务器错误'},status=500)
    if len(obj) == 1:
        bookobj = Book.objects.filter(upload_user = obj[0].UserID)
        l = []
        if bookobj.exists():
            for book in bookobj:
                l.append({'bookname':book.bookname,'book_status':book.book_status,'book_author':book.book_author,'upload_time':book.upload_time,'category':book.category})
        return JsonResponse({'msg':'用户信息',
                                'username':obj[0].Username,
                                'studentid':obj[0].student_id,
                                'book': l,
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

