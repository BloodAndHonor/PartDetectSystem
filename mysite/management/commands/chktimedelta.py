# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from mysite.models import Pic, User,User_Pic_Rel , DtVar ,Queue
from datetime import datetime , timedelta
import urllib2

class Command(BaseCommand):
    args = ''
    help = ''

    #最终评判 返回值为true则不合格 返回值为false为合格
    def isunqualified(self,pic):
        #大于2/3的认为不合格 则不合格 否则合格
        return 3*pic.unqualifiedsum >= 2*pic.votesum


    def sendsignal(self,pic,sg):
        #需要机械臂的接口 sg为true 发送（true）合格信号   sg为false 发送（false）不合格信号
        UNQUALIFIEDURL = ""
        content = ""
        if not sg:
            #对 UNQUALIFIEDURL 发送 http请求
            content = urllib2.urlopen(UNQUALIFIEDURL).read()

    #cron 每隔一段时间 执行的函数
    def handle(self, *args, **options):
        #设定超时60秒 进行最终评判
        DELTATIME = timedelta(0, 60)
        specsdatetime = datetime.now() - DELTATIME
        items = Queue.objects.all().filter(sdatetime__lte=specsdatetime)
        for item in items:
            pic = item.pic
            pic.finished = True
            if self.isunqualified(pic): #不合格
                pic.finaljudge = False
                self.sendsignal(pic,False)
            else: #合格
                pic.finaljudge = True
                self.sendsignal(pic,True)
            pic.save()
            item.delete()