from http.client import responses

from django.contrib.admindocs.utils import ROLES
from django.http import HttpResponse
from django.shortcuts import render
from algorithm import test
from index.models import Role

# Create your views here.


def index(request):
    response = HttpResponse('528图书派送系统后端项目')
    response.status_code = 200
    return response

def login(request):
    return

def signup(request):
    return