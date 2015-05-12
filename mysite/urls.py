# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from mysite import views
urlpatterns = patterns('',
    url(r'^upload$', views.upload, name='upload'),
    url(r'^reg$', views.reg, name='reg'),
    url(r'^login$', views.login, name='login'),
)