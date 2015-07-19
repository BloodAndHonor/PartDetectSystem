#-*- coding:utf-8 -*-
from django.db import models
from datetime import datetime  


#新上传的文件命名格式为 "当前时间.jpg"
def pic_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return '{0}.jpg'.format(str(datetime.now()).replace(':','.'))

#数据库 图片表的定义
class Pic(models.Model):
    # 默认文件路径为 ./staticfile/{id}.jpg
    id = models.AutoField(primary_key=True)
    #上传时间    
    date = models.DateTimeField(db_index=True,default=datetime.now)
    #投票数
    votesum = models.IntegerField(default=0)
    #不合格的投票数
    unqualifiedsum = models.IntegerField(default=0)
    #是否进行过最终评判
    finished = models.BooleanField(db_index=True,default=False)
    #图片文件的位置
    docfile = models.FileField(upload_to=pic_path)
    #是否合格 当finished为true时 finaljudge＝true为合格 finaljudge＝false为不合格
    finaljudge = models.BooleanField(db_index=True,default=False)
    #图片的序列号 唯一标示
    sn = models.CharField(max_length=30,default='')
#数据库 用户表的定义
class User(models.Model):
    id = models.AutoField(primary_key=True)
    #用户名
    username = models.CharField(max_length=30)
    #密码
    password = models.CharField(max_length=30)
    last_logtime = models.DateTimeField(default=datetime.now)

#数据库 用户——图片关系表
class User_Pic_Rel (models.Model):
    id = models.AutoField(primary_key=True)
    #图片
    pic = models.ForeignKey(Pic)
    #用户
    usr = models.ForeignKey(User)
    #是否不合格 true为不合格 false为合格
    unqualified = models.BooleanField(default=True)

#弃用 不要动它了 没有什么实际意义 但不要动它
class DtVar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10,db_index=True,blank=True)
    val = models.DateTimeField(default=datetime.now)

#数据库 评判队列表 pic.finished为false的图片集
class Queue(models.Model):
    id = models.AutoField(primary_key=True)
    #图片
    pic = models.ForeignKey(Pic)
    #第一个用户对该图片进行评判的时间 用来计算这个图片从开始评判到现在的时间 用来判断是否超过特定时间然后进行最终评判
    sdatetime = models.DateTimeField(default=datetime.now)