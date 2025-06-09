from django.db import models

# Create your models here.

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20, unique=True)
    real_name = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=20, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

class Book(models.Model):
    ISBN = models.CharField(max_length=13, primary_key=True)
    bookname = models.CharField(max_length=13, unique=True)
    book_author = models.CharField(max_length=13, unique=True)
    book_status = models.IntegerField(default=0) #状态0为可借、状态1为已借出、状态2为下架
    upload_time = models.DateTimeField(auto_now_add=True)
    upload_user = models.ForeignKey('User', on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    # category = models.CharField(max_length=13, unique=True)   分为多少类


