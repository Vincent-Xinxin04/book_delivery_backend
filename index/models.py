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

class Role(models.Model):
    Role_ID = models.CharField(max_length=11, primary_key=True)
    Role_name = models.CharField(max_length=20, unique=True)

class Permission(models.Model):
    Perm_ID = models.CharField(max_length=11, primary_key=True)
    Perm_name = models.CharField(max_length=50, unique=True)
    Perm_desc = models.CharField(max_length=100, unique=True)

class Book(models.Model):
    Book_ID = models.CharField(max_length=13, primary_key=True)
    bookname = models.CharField(max_length=13, unique=True)
    book_author = models.CharField(max_length=13, unique=True)
    book_status = models.IntegerField(default=0) #状态0为可借、状态1为已借出、状态2为下架
    upload_time = models.DateTimeField(auto_now_add=True)
    upload_user = models.ForeignKey('User', on_delete=models.CASCADE)
    category = models.CharField(max_length=13, unique=True,default='NULL')    #分为多少类

class Order(models.Model):
    Order_ID = models.CharField(max_length=32, primary_key=True)
    UserID = models.ForeignKey('User', on_delete=models.CASCADE, related_name='user_orders')
    book_ID = models.ForeignKey('Book', on_delete=models.CASCADE)
    courier_ID = models.ForeignKey('User', on_delete=models.CASCADE, related_name='courier_orders')
    order_status = models.CharField(max_length=20,default='待处理')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

class User_Role(models.Model):
    User_ID = models.ForeignKey('User', on_delete=models.CASCADE)
    Role_ID = models.ForeignKey('Role', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('User_ID', 'Role_ID')  # 确保组合唯一

class Role_Permission(models.Model):
    Role_ID = models.ForeignKey('Role', on_delete=models.CASCADE)
    Perm_ID = models.ForeignKey('Permission', on_delete=models.CASCADE)
    class Meta:
        unique_together = ('Role_ID', 'Perm_ID')  # 确保组合唯一

