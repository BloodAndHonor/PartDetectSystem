#-*- coding:utf-8 -*-
from django.db import models
import datetime
# Create your models here.

class Pic(models.Model):
	#默认文件路径为 ./staticfile/{id}.jpg
	id = models.AutoField(primary_key = True)
	date = models.DateField(default = datetime.datetime.now())
	ratesum = models.IntegerField(default = 0)
	qualifiedsum = models.IntegerField(default = 0)

class User(models.Model):
	id = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 30)
	password = models.CharField(max_length = 30)
	last_logtime = models.DateField()

class User_Pic_Rel (models.Model):
	id = models.AutoField(primary_key = True)
	picid = models.IntegerField(db_index = True, default = 0)
	uid = models.IntegerField(db_index = True, default = 0)
	qualified = models.BooleanField(default = False)


