"""
URL configuration for book_delivery_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index import views as index_views
from monitor import views as monitor_views
from user import views as user_views
from volunteer import views as volunteer_views
urlpatterns = [
    path('index/', index_views.index),

    #Maybe登录注册？
    path('login/',index_views.login),

    path('signup/',index_views.signup),

    #个人信息的展示
    path('profile/',user_views.profile),

    path('profile/update/',user_views.update),

    #志愿者申请派单
    path('volunteer/',volunteer_views.order),


]
