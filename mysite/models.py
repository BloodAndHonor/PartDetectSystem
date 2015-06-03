#-*- coding:utf-8 -*-
from django.db import models
from datetime import datetime  

# Create your models here.

def pic_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}.jpg'.format(str(datetime.now()).replace(':','.'))


class Pic(models.Model):
    # 默认文件路径为 ./staticfile/{id}.jpg
    id = models.AutoField(primary_key=True)    
    date = models.DateTimeField(db_index=True,default=datetime.now)
    votesum = models.IntegerField(default=0)
    unqualifiedsum = models.IntegerField(default=0)
    finished = models.BooleanField(db_index=True,default=False)
    docfile = models.FileField(upload_to=pic_path)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    last_logtime = models.DateTimeField(default=datetime.now)


class User_Pic_Rel (models.Model):
    id = models.AutoField(primary_key=True)
    pic = models.ForeignKey(Pic)
    usr = models.ForeignKey(User)
    unqualified = models.BooleanField(default=True)

class DtVar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10,db_index=True,blank=True)
    val = models.DateTimeField(default=datetime.now)
