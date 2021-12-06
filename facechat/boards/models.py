from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    #password=models.CharField(max_length=200)
    
class User_f(models.Model):
    usename_f=models.CharField(max_length=16)
    email_f=models.EmailField()
    pass_f=models.CharField(max_length=16)
    #compass_f=models.CharField(max_length=16)
class Post_f(models.Model):
    user_f_id = models.ForeignKey(User_f, on_delete=models.CASCADE)
    text_f=models.TextField()
#ชื่อต่อกับ auth_user table
class Post_f_a(models.Model):
        authuser_f_id = models.ForeignKey(User,on_delete=models.CASCADE)
        text_f=models.TextField()

