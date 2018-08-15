from django.shortcuts import render
from lecture.models import timetable
import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def ttdisp(request):
    dicti = dict()
    if request.user.is_staff == True:
        dicti['su'] = True
    insti = request.user.profile.institute
    yr = request.user.profile.year
    if insti == 'LNMIIT':
        dicti['mis'] = "https://erp.lnmiit.ac.in/mis/"
        dicti['lib'] = "https://172.22.2.26/opac/"
    else:
        dicti['mis'] = '#'
        dicti['lib'] = '#'
    now = datetime.datetime.now()
    t = now.strftime("%H:%M:%S")
    d = now.strftime("%A")
    dicti['current'] = timetable.objects.filter(institute=insti,year=yr,day=d,sltst__lte=t,slten__gte=t).order_by('sltst')
    temp = timetable.objects.filter(institute=insti,year=yr,day=d,sltst__gte=t).order_by('sltst')
    if len(temp)>0:
        ti = temp[0].sltst
        dicti['next'] = timetable.objects.filter(institute=insti,year=yr,day=d,sltst=ti).order_by('sltst')
    if len(dicti['current'])==0 and len(temp)==0:
        dicti['noclass']=True
    return render(request,'lecture/timetable.html',context=dicti)
