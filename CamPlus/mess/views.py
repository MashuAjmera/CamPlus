from django.shortcuts import render
from mess.models import menu
import datetime

# Create your views here.
def timebetween(on_time, off_time):
    time_to_check = datetime.datetime.now().time()
    print(on_time,time_to_check,off_time)
    if time_to_check >= on_time and time_to_check <= off_time:
        return True
    else:
        return False

def menudisp(request):
    dy=datetime.datetime.now().strftime("%A")
    men=menu.objects.get(day=dy)
    brk = men.brk
    lun = men.lun
    snk = men.snk
    din = men.din
    dicti = dict()
    if timebetween(datetime.time(00,00),datetime.time(7,00)):
        dicti['brk'] = brk
        dicti['lun'] = lun
        dicti['snk'] = snk
        dicti['din'] = din
    elif timebetween(datetime.time(7,00),datetime.time(9,30)):
        dicti['cur'] = brk
        value = datetime.datetime.combine(datetime.date.today(),datetime.time(9,30)) - datetime.datetime.now()
        dicti['timeleft'] = (datetime.datetime.min + value).time()
        dicti['lun'] = lun
        dicti['snk'] = snk
        dicti['din'] = din
    elif timebetween(datetime.time(9,30),datetime.time(12,00)):
        dicti['lun'] = lun
        dicti['snk'] = snk
        dicti['din'] = din
    elif timebetween(datetime.time(12,00),datetime.time(14,30)):
        dicti['cur'] = lun
        value = datetime.datetime.combine(datetime.date.today(),datetime.time(14,30)) - datetime.datetime.now()
        dicti['timeleft'] = (datetime.datetime.min + value).time()
        print(dicti['timeleft'])
        dicti['snk'] = snk
        dicti['din'] = din
    elif timebetween(datetime.time(14,30),datetime.time(17,15)):
        dicti['snk'] = snk
        dicti['din'] = din
    elif timebetween(datetime.time(17,15),datetime.time(18,15)):
        dicti['cur'] = snk
        value = datetime.datetime.combine(datetime.date.today(),datetime.time(18,15)) - datetime.datetime.now()
        dicti['timeleft'] = (datetime.datetime.min + value).time()
        dicti['din'] = din
    elif timebetween(datetime.time(18,15),datetime.time(19,30)):
        dicti['din'] = din
    elif timebetween(datetime.time(19,30),datetime.time(21,30)):
        dicti['cur'] = din
        value = datetime.datetime.combine(datetime.date.today(),datetime.time(21,30)) - datetime.datetime.now()
        dicti['timeleft'] = (datetime.datetime.min + value).time()
    else:
        dicti['end'] = "Sorry College Will Not Be Providing Any More Meals For The Day."

    return render(request,'mess/menu.html',context = dicti)
