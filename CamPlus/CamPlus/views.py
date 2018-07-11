from django.shortcuts import render
import datetime
from lecture.models import timetable
from mess.models import menu
from trans.models import buswd,buswe
from django.contrib.auth.decorators import login_required
# Create your views here.

def timebetween(on_time, off_time):
    time_to_check = datetime.datetime.now().time()
    if time_to_check >= on_time and time_to_check <= off_time:
        return True
    else:
        return False

@login_required
def index(request):
    insti = request.user.profile.institute
    yr = request.user.profile.year
    now = datetime.datetime.now()
    dy=now.strftime("%A")
    tim = now.strftime("%H:%M:%S")
    dicti = dict()
    if request.user.is_staff == True:
        dicti['su'] = True
    dicti['name'] = request.user.first_name+' '+ request.user.last_name
    dicti['none']=True
    if insti == 'LNMIIT':
        dicti['mis'] = "https://erp.lnmiit.ac.in/mis/"
    else:
        dicti['mis'] = '#'
    try:
        men=menu.objects.get(institute=insti,day=dy)
        brk = men.brk
        lun = men.lun
        snk = men.snk
        din = men.din
        if timebetween(datetime.time(7,00),datetime.time(9,30)):
            dicti['cur'] = brk
            dicti['none']=False
            value = datetime.datetime.combine(datetime.date.today(),datetime.time(9,30)) - datetime.datetime.now()
            dicti['timeleft'] = (datetime.datetime.min + value).time()
        elif timebetween(datetime.time(12,00),datetime.time(14,30)):
            dicti['cur'] = lun
            dicti['none']=False
            value = datetime.datetime.combine(datetime.date.today(),datetime.time(14,30)) - datetime.datetime.now()
            dicti['timeleft'] = (datetime.datetime.min + value).time()
        elif timebetween(datetime.time(17,15),datetime.time(18,15)):
            dicti['cur'] = snk
            dicti['none']=False
            value = datetime.datetime.combine(datetime.date.today(),datetime.time(18,15)) - datetime.datetime.now()
            dicti['timeleft'] = (datetime.datetime.min + value).time()
        elif timebetween(datetime.time(19,30),datetime.time(21,30)):
            dicti['cur'] = din
            dicti['none']=False
            value = datetime.datetime.combine(datetime.date.today(),datetime.time(21,30)) - datetime.datetime.now()
            dicti['timeleft'] = (datetime.datetime.min + value).time()
    except:
        pass

    dicti['current'] = timetable.objects.filter(institute=insti,year=yr,day=dy,sltst__lte=tim,slten__gte=tim).order_by('sltst')
    temp = timetable.objects.filter(institute=insti,year=yr,day=dy,sltst__gte=tim).order_by('sltst')
    if len(temp)>0:
        ti = temp[0].sltst
        dicti['next'] = timetable.objects.filter(institute=insti,year=yr,day=dy,sltst=ti).order_by('sltst')
    if len(dicti['current']) !=0 or len(temp) !=0:
        dicti['none']=False

    try:
        if dy != 'Sunday':
            try:
                dicti['latest']= buswd.objects.filter(institute=insti,time__gte=tim).order_by('time')[0]
            except:
                pass
            if dicti['latest']:
                dicti['none']=False
        else:
            try:
                dicti['latest']= buswe.objects.filter(institute=insti,time__gte=tim).order_by('time')[0]
            except:
                pass
            if dicti['latest']:
                dicti['none']=False
    except:
        pass

    return render(request,'index.html',context=dicti)
