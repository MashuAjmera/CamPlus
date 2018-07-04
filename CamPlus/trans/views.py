from django.shortcuts import render
from trans.models import buswd,buswe
import datetime
from trans import busentry
from django.db.models import Q

# Create your views here.
def bus(request):
    dicti = dict()
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    if now.strftime("%A") != 'Sunday':
        qlist = buswd.objects.filter(time__gte=t).order_by('time')
    else:
        qlist = buswe.objects.filter(time__gte=t).order_by('time')
    if len(qlist) > 0:
        dicti['latest']=qlist[0]
        if len(qlist) >1:
            dicti['buslst']=qlist[1:]
    return render(request,'trans/bus.html',context=dicti)

def buslnm(request):
    dicti = dict()
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    if now.strftime("%A") != 'Sunday':
        dicti['latest']= buswd.objects.filter(time__gte=t).order_by('time')[0]
        dicti['buslst'] = buswd.objects.filter(time__gte=t,frm='LNMIIT').order_by('time')
    else:
        dicti['latest']= buswe.objects.filter(time__gte=t).order_by('time')[0]
        dicti['buslst'] = buswe.objects.filter(time__gte=t,frm='LNMIIT').order_by('time')
    # if len(qlist) > 0:
    #     dicti['latest']=qlist[0]
    #     if len(qlist) >1:
    #         dicti['buslst']=qlist[1:]
    return render(request,'trans/bus.html',context=dicti)

def buscit(request):
    dicti = dict()
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    if now.strftime("%A") != 'Sunday':
        dicti['latest']= buswd.objects.filter(time__gte=t).order_by('time')[0]
        dicti['buslst'] = buswd.objects.filter(time__gte=t,to='LNMIIT').order_by('time')
    else:
        dicti['latest']= buswe.objects.filter(time__gte=t).order_by('time')[0]
        dicti['buslst'] = buswe.objects.filter(time__gte=t,to='LNMIIT').order_by('time')
    # if len(qlist) > 0:
    #     dicti['latest']=qlist[0]
    #     if len(qlist) >1:
    #         dicti['buslst']=qlist[1:]
    return render(request,'trans/bus.html',context=dicti)

def busoth(request):
    dicti = dict()
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    if now.strftime("%A") != 'Sunday':
        dicti['latest']= buswd.objects.filter(time__gte=t).order_by('time')[0]
        dicti['buslst'] = buswd.objects.filter(Q(time__gte=t) & ~Q(frm='LNMIIT') & ~Q(to='LNMIIT')).order_by('time')
    else:
        dicti['latest']= buswe.objects.filter(time__gte=t).order_by('time')[0]
        dicti['buslst'] = buswe.objects.filter(Q(time__gte=t) & ~Q(frm='LNMIIT') & ~Q(to='LNMIIT')).order_by('time')
    # if len(qlist) > 0:
    #     dicti['latest']=qlist[0]
    #     if len(qlist) >1:
    #         dicti['buslst']=qlist[1:]
    return render(request,'trans/bus.html',context=dicti)
