# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from mysite import views
urlpatterns = patterns('',
    url(r'^tst$', views.tst, name='tst'),
)