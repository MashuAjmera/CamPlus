from django.shortcuts import render
import datetime
from lecture.models import timetable
from mess.models import menu
from trans.models import buswd,buswe
# Create your views here.

def timebetween(on_time, off_time):
    time_to_check = datetime.datetime.now().time()
    print(on_time,time_to_check,off_time)
    if time_to_check >= on_time and time_to_check <= off_time:
        return True
    else:
        return False

def index(request):
    now = datetime.datetime.now()
    dy=now.strftime("%A")
    tim = now.strftime("%H:%M:%S")
    dicti = dict()

    men=menu.objects.get(day=dy)
    brk = men.brk
    lun = men.lun
    snk = men.snk
    din = men.din
    if timebetween(datetime.time(7,00),datetime.time(9,30)):
        dicti['cur'] = brk
        value = datetime.datetime.combine(datetime.date.today(),datetime.time(9,30)) - datetime.datetime.now()
        dicti['timeleft'] = (datetime.datetime.min + value).time()
    elif timebetween(datetime.time(12,00),datetime.time(14,30)):
        dicti['cur'] = lun
        value = datetime.datetime.combine(datetime.date.today(),datetime.time(14,30)) - datetime.datetime.now()
        dicti['timeleft'] = (datetime.datetime.min + value).time()
    elif timebetween(datetime.time(17,15),datetime.time(18,15)):
        dicti['cur'] = snk
        value = datetime.datetime.combine(datetime.date.today(),datetime.time(18,15)) - datetime.datetime.now()
        dicti['timeleft'] = (datetime.datetime.min + value).time()
    elif timebetween(datetime.time(19,30),datetime.time(21,30)):
        dicti['cur'] = din
        value = datetime.datetime.combine(datetime.date.today(),datetime.time(21,30)) - datetime.datetime.now()
        dicti['timeleft'] = (datetime.datetime.min + value).time()

    dicti['timetab'] = timetable.objects.filter(day=dy,sltst__lte=tim,slten__gte=tim).order_by('year','sltst')

    if dy != 'Sunday':
        dicti['latest']= buswd.objects.filter(time__gte=tim).order_by('time')[0]
    else:
        dicti['latest']= buswe.objects.filter(time__gte=tim).order_by('time')[0]

    return render(request,'index.html',context=dicti)
