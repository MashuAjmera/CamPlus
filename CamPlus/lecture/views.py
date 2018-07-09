from django.shortcuts import render
from lecture.models import timetable
import datetime
# Create your views here.

def ttdisp(request):
    dicti = dict()
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    d = now.strftime("%A")
    print(t,d)
    dicti['timetab'] = timetable.objects.filter(day=d,sltst__lte=t,slten__gte=t).order_by('year','sltst')
    return render(request,'lecture/timetable.html',context=dicti)
