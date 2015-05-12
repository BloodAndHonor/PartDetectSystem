# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404,render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext, loader
from django.forms import ModelForm
from django.core.context_processors import csrf
import random
from mysite.forms import DocumentForm,RegForm,LoginForm
from mysite.models import User_Pic_Rel,User,Pic,DtVar
# Create your views here.
from datetime import datetime
def init(request):
   DtVar.objects.all().delete()
   DtVar(name='sdate',val=datetime.now()).save()
   DtVar(name='tdate',val=datetime.now()).save()
def setspan(request,sy,sm,sd,sh,smin,ssec,ty,tm,td,th,tmin,tsec):
    sdate = get_object_or_404(DtVar,name='sdate')
    tdate = get_object_or_404(DtVar,name='tdate')
    sdate.val=datetime(sy,sm,sd,sh,smin,ssec,0)
    tdate.val=datetime(ty,tm,td,th,tmin,tsec,0)
    sdate.save()
    tdate.save()

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Pic(docfile=request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect(reverse('mysite:upload'))
    form = DocumentForm()
    documents=Pic.objects.all()
    return render_to_response(
        'mysite/upload.html',
        {'form':form,'documents':documents},
        context_instance=RequestContext(request)
    )
def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = RegForm(request.POST)
        if form.is_valid():
            qry_usrs = User.objects.all().filter(username=username)
            if len(qry_usrs) != 0:
                return HttpResponse('用户已存在！')
            newusr = User(username=request.POST['username'],password=request.POST['password'])
            newusr.save()
            return HttpResponseRedirect(reverse('mysite:reg'))    
    form = RegForm()
    usrs=User.objects.all()
    c={
        'form':form,
        'usrs':usrs,
    }
    return render_to_response('mysite/reg.html',c,context_instance=RequestContext(request))

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = LoginForm(request.POST)
        if form.is_valid():
            qry_usrs = User.objects.all().filter(username=username).filter(password=password)
            if len(qry_usrs) == 1:
                return HttpResponse('登录成功')
    form = LoginForm()
    c= {
        'form':form,
    }
    return render_to_response('mysite/login.html',c,context_instance=RequestContext(request))
