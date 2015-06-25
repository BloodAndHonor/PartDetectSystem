# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from mysite import views
urlpatterns = patterns('',
                       url(r'upload$', views.upload, name='upload'),
                       url(r'reg$', views.reg, name='reg'),
                       url(r'login$', views.login, name='login'),
                       # setspan(request,sy,sm,sd,sh,smin,ssec,ty,tm,td,th,tmin,tsec):
                       url(
                           r'setspan/(?P<sy>\d+)/(?P<sm>\d+)/(?P<sd>\d+)/(?P<sh>\d+)/(?P<smin>\d+)/(?P<ssec>\d+)/(?P<ty>\d+)/(?P<tm>\d+)/(?P<td>\d+)/(?P<th>\d+)/(?P<tmin>\d+)/(?P<tsec>\d+)',views.setspan,name='setspan')
                       ,
                       url(r'init$',views.init,name='init'),
                       url(r'validpics$',views.validpics,name='validpics'),
                       url(r'ufinpics$',views.ufinpics,name='ufinpics'),
                       url(r'finpics$',views.finpics,name='finpics'),
                       url(r'finpics/(?P<page>\d+)$',views.finpics,name='finpics'),
                       url(r'ufinpics/(?P<page>\d+)$',views.ufinpics,name='ufinpics'),
                       url(r'gopageufin$',views.gopageufin,name='gopageufin'),
                       )
