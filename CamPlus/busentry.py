import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CamPlus.settings')

import django
django.setup()

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

import datetime
import time

from trans.models import buswd,buswe

def busupdate():
    buswd.objects.filter(institute = 'LNMIIT').delete()
    buswe.objects.filter(institute = 'LNMIIT').delete()

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = "https://www.lnmiit.ac.in/Bus_Time_Table.html"
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tablelst = soup.find_all('table', attrs={'class':'table-data'})

    data = []

    we = 0

    for table in tablelst:
        table_body = table.find('tbody')

        data = []

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        for colmn in data[2:]:
            if len(colmn)>0:
                time = colmn[1]
                time = time.split()
                t=time[1]
                time = time[0].split(':')
                if t == 'PM' and time[0]!='12':
                    time[0] = str(int(time[0])+12)
                if we==0:
                    if colmn[2] != '-----':
                        buswd.objects.create(institute = 'LNMIIT',frm=colmn[2],to=colmn[3],time=datetime.datetime.strptime(time[0]+':'+time[1],'%H:%M').time(),busno=colmn[4],operator='LNMIIT')
                    if colmn[5] != '-----':
                        buswd.objects.create(institute = 'LNMIIT',frm=colmn[5],to=colmn[6],time=datetime.datetime.strptime(time[0]+':'+time[1],'%H:%M'),operator='Government')
                else:
                    buswe.objects.create(institute = 'LNMIIT',frm=colmn[2],to=colmn[3],time=datetime.datetime.strptime(time[0]+':'+time[1],'%H:%M').time(),busno=colmn[4],operator='LNMIIT')
        we = 1

if __name__ == '__main__':
    print("Updating Bus")
    busupdate()
    print("Updated Bus")
