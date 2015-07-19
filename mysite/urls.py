# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from mysite import views

#url和view.py中的函数进行关联
urlpatterns = patterns('',
                       # http://{ip地址}/upload 
                       #上传图片
                       url(r'upload$', views.upload, name='upload'),
                       #http://{ip地址}/reg
                       #用户注册
                       url(r'reg$', views.reg, name='reg'),
                       #http://{ip地址}/login 
                       #用户登录
                       url(r'login$', views.login, name='login'),
                       url(
                           r'setspan/(?P<sy>\d+)/(?P<sm>\d+)/(?P<sd>\d+)/(?P<sh>\d+)/(?P<smin>\d+)/(?P<ssec>\d+)/(?P<ty>\d+)/(?P<tm>\d+)/(?P<td>\d+)/(?P<th>\d+)/(?P<tmin>\d+)/(?P<tsec>\d+)',views.setspan,name='setspan')
                       ,
                       #http://{ip地址}/init 
                       #清空数据库数据
                       url(r'init$',views.init,name='init'),
                       #http://{ip地址}/validpics 
                       #得到当前登陆用户可以进行评判的图片集
                       url(r'validpics$',views.validpics,name='validpics'),
                       #http://{ip地址}/ufinpics 
                       #得到所有未进行最终评判的图片集
                       url(r'ufinpics$',views.ufinpics,name='ufinpics'),
                       #http://{ip地址}/finpics
                       #得到所有已经被最终评判的图片集 
                       url(r'finpics$',views.finpics,name='finpics'),
                       url(r'finpics/(?P<page>\d+)$',views.finpics,name='finpics'),
                       url(r'ufinpics/(?P<page>\d+)$',views.ufinpics,name='ufinpics'),
                       url(r'gopageufin$',views.gopageufin,name='gopageufin'),
                       )
