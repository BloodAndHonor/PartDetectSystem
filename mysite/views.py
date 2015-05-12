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
from mysite.models import Document
from mysite.forms import DocumentForm
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

def tst(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Pic(docfile=request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect(reverse('mysite.views.tst'))
    else:
        form = DocumentForm()
        documents=Pic.objects.all()
        return render_to_response(
            'mysite/tst.html',
            {'form':form,'documents':documents},
            context_instance=RequestContext(request)
        )
