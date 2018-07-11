from django.shortcuts import render
from trans.models import buswd,buswe
import datetime
from trans import busentry
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def bus(request):
    dicti = dict()
    if request.user.is_staff == True:
        dicti['su'] = True
    insti = request.user.profile.institute
    if insti == 'LNMIIT':
        dicti['mis'] = "https://erp.lnmiit.ac.in/mis/"
    else:
        dicti['mis'] = '#'
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    if now.strftime("%A") != 'Sunday':
        qlist = buswd.objects.filter(institute=insti,time__gte=t).order_by('time')
    else:
        qlist = buswe.objects.filter(institute=insti,time__gte=t).order_by('time')
    if len(qlist) > 0:
        dicti['latest']=qlist[0]
        if len(qlist) >1:
            dicti['buslst']=qlist
    return render(request,'trans/bus.html',context=dicti)

@login_required
def buslnm(request):
    dicti = dict()
    if request.user.is_staff == True:
        dicti['su'] = True
    insti = request.user.profile.institute
    if insti == 'LNMIIT':
        dicti['mis'] = "https://erp.lnmiit.ac.in/mis/"
    else:
        dicti['mis'] = '#'
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    try:
        if now.strftime("%A") != 'Sunday':
            dicti['latest']= buswd.objects.filter(institute=insti,time__gte=t).order_by('time')[0]
            dicti['buslst'] = buswd.objects.filter(institute=insti,time__gte=t,frm='LNMIIT').order_by('time')
        else:
            dicti['latest']= buswe.objects.filter(institute=insti,time__gte=t).order_by('time')[0]
            dicti['buslst'] = buswe.objects.filter(institute=insti,time__gte=t,frm='LNMIIT').order_by('time')
    except:
        pass
    # if len(qlist) > 0:
    #     dicti['latest']=qlist[0]
    #     if len(qlist) >1:
    #         dicti['buslst']=qlist[1:]
    return render(request,'trans/bus.html',context=dicti)

@login_required
def buscit(request):
    dicti = dict()
    if request.user.is_staff == True:
        dicti['su'] = True
    insti = request.user.profile.institute
    if insti == 'LNMIIT':
        dicti['mis'] = "https://erp.lnmiit.ac.in/mis/"
    else:
        dicti['mis'] = '#'
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    try:
        if now.strftime("%A") != 'Sunday':
            dicti['latest']= buswd.objects.filter(institute=insti,time__gte=t).order_by('time')[0]
            dicti['buslst'] = buswd.objects.filter(institute=insti,time__gte=t,to='LNMIIT').order_by('time')
        else:
            dicti['latest']= buswe.objects.filter(institute=insti,time__gte=t).order_by('time')[0]
            dicti['buslst'] = buswe.objects.filter(institute=insti,time__gte=t,to='LNMIIT').order_by('time')
    except:
        pass
    # if len(qlist) > 0:
    #     dicti['latest']=qlist[0]
    #     if len(qlist) >1:
    #         dicti['buslst']=qlist[1:]
    return render(request,'trans/bus.html',context=dicti)

@login_required
def busoth(request):
    dicti = dict()
    if request.user.is_staff == True:
        dicti['su'] = True
    insti = request.user.profile.institute
    if insti == 'LNMIIT':
        dicti['mis'] = "https://erp.lnmiit.ac.in/mis/"
    else:
        dicti['mis'] = '#'
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    try:
        if now.strftime("%A") != 'Sunday':
            dicti['latest']= buswd.objects.filter(institute=insti,time__gte=t).order_by('time')[0]
            dicti['buslst'] = buswd.objects.filter(Q(institute=insti) & Q(time__gte=t) & ~Q(frm='LNMIIT') & ~Q(to='LNMIIT')).order_by('time')
        else:
            dicti['latest']= buswe.objects.filter(institute=insti,time__gte=t).order_by('time')[0]
            dicti['buslst'] = buswe.objects.filter(Q(institute=insti) & Q(time__gte=t) & ~Q(frm='LNMIIT') & ~Q(to='LNMIIT')).order_by('time')
    except:
        pass
    # if len(qlist) > 0:
    #     dicti['latest']=qlist[0]
    #     if len(qlist) >1:
    #         dicti['buslst']=qlist[1:]
    return render(request,'trans/bus.html',context=dicti)
