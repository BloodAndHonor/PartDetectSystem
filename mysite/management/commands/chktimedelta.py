# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from mysite.models import Pic, User,User_Pic_Rel , DtVar ,Queue
from datetime import datetime , timedelta
import urllib2

class Command(BaseCommand):
    args = ''
    help = ''

    def isunqualified(self,pic):
        return 3*pic.unqualifiedsum >= 2*pic.votesum

    def sendsignal(self,pic,sg):
        #需要机械臂的接口
        UNQUALIFIEDURL = ""
        content = ""
        if not sg:
            content = urllib2.urlopen(UNQUALIFIEDURL).read()


    def handle(self, *args, **options):
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