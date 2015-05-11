#-*- coding:utf-8 -*-
from django.db import models
from datetime import datetime  

# Create your models here.


class Pic(models.Model):
    # 默认文件路径为 ./staticfile/{id}.jpg
    id = models.AutoField(primary_key=True)    
    date = models.DateTimeField(db_index=True,default=datetime.now)
    votesum = models.IntegerField(default=0)
    unqualifiedsum = models.IntegerField(default=0)
    finished = models.BooleanField(db_index=True,default=False)
    docfile = models.FileField(upload_to='pic/%Y/%m/%d',default='settings.MEDIA_ROOT/anonymous.jpg')


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    last_logtime = models.DateTimeField(default=datetime.now)


class User_Pic_Rel (models.Model):
    id = models.AutoField(primary_key=True)
    picid = models.IntegerField(db_index=True, default=0)
    uid = models.IntegerField(db_index=True, default=0)
    unqualified = models.BooleanField(default=True)

class DtVar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10,db_index=True,blank=True)
    val = models.DateTimeField(default=datetime.now)
    
class Document(models.Model):
    docfile = models.FileField(upload_to='pic/%Y/%m/%d',default='settings.MEDIA_ROOT/anonymous.jpg')