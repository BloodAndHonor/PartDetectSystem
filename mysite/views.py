# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext, loader
from django.forms import ModelForm
from django.core.context_processors import csrf
import random

from mysite.forms import DocumentForm, RegForm, LoginForm
from mysite.models import User_Pic_Rel, User, Pic, DtVar , Queue

from datetime import datetime



def init(request):
    #删除数据库所有数据
    DtVar.objects.all().delete()
    DtVar(name='sdate', val=datetime.now()).save()
    DtVar(name='tdate', val=datetime.now()).save()
    Pic.objects.all().delete()
    User.objects.all().delete()
    User_Pic_Rel.objects.all().delete()
    Queue.objects.all().delete()
    return HttpResponse('OK!')
#


def setspan(request, sy, sm, sd, sh, smin, ssec, ty, tm, td, th, tmin, tsec):
    #这个没用 可以不看
    sdate = get_object_or_404(DtVar, name='sdate')
    tdate = get_object_or_404(DtVar, name='tdate')
    sdate.val = datetime(
        int(sy), int(sm), int(sd), int(sh), int(smin), int(ssec), 0)
    tdate.val = datetime(
        int(ty), int(tm), int(td), int(th), int(tmin), int(tsec), 0)
    sdate.save()
    tdate.save()
    return HttpResponse('ok!')


@csrf_exempt
def upload(request):
    #上传图片
    #对应的网页模版地址为 mysite/templates/mysite/upload.html
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            tsn=request.FILES['docfile'].name
            newdoc = Pic(docfile=request.FILES['docfile'],sn=tsn)
            newdoc.save()
            return HttpResponseRedirect(reverse('mysite:upload'))
    form = DocumentForm()
    documents = Pic.objects.all()
    return render_to_response(
        'mysite/upload.html',
        {'form': form, 'documents': documents},
        context_instance=RequestContext(request)
    )


@csrf_exempt
def reg(request):
    #注册用户
    #对应的网页模版地址为 mysite/templates/mysite/reg.html
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = RegForm(request.POST)
        if form.is_valid():
            qry_usrs = User.objects.all().filter(username=username)
            if len(qry_usrs) != 0:
                return HttpResponse('用户已存在！')
            newusr = User(
                username=request.POST['username'], password=request.POST['password'])
            newusr.save()
            return HttpResponseRedirect(reverse('mysite:reg'))
    form = RegForm()
    usrs = User.objects.all()
    c = {
        'form': form,
        'usrs': usrs,
    }
    return render_to_response('mysite/reg.html', c, context_instance=RequestContext(request))



@csrf_exempt
def login(request):
    #用户登录
    #对应的模版地址为 mysite/templates/mysite/login.html
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        form = LoginForm(request.POST)
        if form.is_valid():
            qry_usrs = User.objects.all().filter(
                username=username).filter(password=password)
            if len(qry_usrs) == 1:
                request.session['username'] = username
                request.session['password'] = password
                return HttpResponse('登录成功')
    form = LoginForm()
    c = {
        'form': form,
    }
    return render_to_response('mysite/login.html', c, context_instance=RequestContext(request))
# 检查cookies


def chkcookies(request):
    #检查cookies是否合法
    username = request.session.get('username', None)
    password = request.session.get('password', None)
    if username and password:
        qry_usrs = User.objects.all().filter(
            username=username).filter(password=password)
        if len(qry_usrs) == 1:
            return qry_usrs[0]
        else:
            return None
    else:
        return None



@csrf_exempt
def validpics(request):
    #返回当前登陆用户可以进行判定的图片集
    #对应的模版地址为 mysite/templates/mysite/show.html
    usr = chkcookies(request)
    if usr == None:
        return HttpResponse('请先登录！')
    if request.method != 'POST':
        sdate = get_object_or_404(DtVar, name='sdate').val
        tdate = get_object_or_404(DtVar, name='tdate').val
        pics = Pic.objects.all().filter(date__gt=sdate).filter(finished=False).exclude(
            id__in=User_Pic_Rel.objects.all().filter(usr=usr).values_list('pic', flat=True))[:1]
        c = {}
        if pics:
            curpic = pics[0]

            c = {
                'curpic': curpic,
            }
        return render_to_response('mysite/show.html', c, context_instance=RequestContext(request))

    else:
        opt = request.POST['judge']
        picid = int(request.POST['picid'])
        pic = get_object_or_404(Pic, id=picid)
        pic.votesum += 1
        if opt == ('合格'.decode('utf8')):
            User_Pic_Rel(pic=pic, usr=usr, unqualified=0).save()            
        else:
            pic.unqualifiedsum += 1
            User_Pic_Rel(pic=pic, usr=usr, unqualified=1).save()
            
	qres = Queue.objects.all().filter(pic=pic)
	if len(qres) == 0 :
	    Queue(pic=pic,sdatetime=datetime.now()).save()
        else:
    	    qres[0].sdatetime=datetime.now()
	    qres[0].save()
        pic.save()
        return HttpResponseRedirect(reverse('mysite:validpics'))


@csrf_exempt
def ufinpics(request,page=1):
    #得到所有未进行最终评判的图片集
    #对应的模版地址为 mysite/templates/mysite/ufinpics.html
    pics = Queue.objects.all()
    paginator=Paginator(pics,25)
    try:
        partcontext = paginator.page(page)
    except PageNotAnInteger:
        partcontext = paginator.page(1)
    except EmptyPage:
        partcontext=paginator.page(paginator.num_pages)
    c={'items':partcontext}
    return render_to_response('mysite/ufinpics.html',c,context_instance=RequestContext(request))
@csrf_exempt
def gopageufin(request):
    return ufinpics(request,request.POST['pagenum'])

@csrf_exempt
def finpics(request,page=1):
    #得到已经进行最终评判的图片集
    #对应的模版地址为 mysite/templates/mysite/finpics.html
    pics = Pic.objects.all().filter(finished=True)
    paginator=Paginator(pics,25)
    try:
        partcontext = paginator.page(page)
    except PageNotAnInteger:
        partcontext = paginator.page(1)
    except EmptyPage:
        partcontext = paginator.page(paginator.num_pages)
    c={'items':partcontext}
    return render_to_response('mysite/finpics.html',c,context_instance=RequestContext(request))
@csrf_exempt
def gopagefin(request):
    return finpics(request,request.POST['pagenum']) 

