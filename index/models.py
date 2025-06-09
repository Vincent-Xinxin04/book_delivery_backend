from django.db import models

# Create your models here.

class User:
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10, unique=True)
    real_name = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=10, unique=True)