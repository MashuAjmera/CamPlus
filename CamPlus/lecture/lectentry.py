import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CamPlus.settings')

import django
django.setup()

from lecture.models import timetable
import datetime


def timetableupd():
    timetable.objects.all().delete()
    timetable.objects.create(day='Monday',LT='LT2',sltst=datetime.datetime.strptime("8:00",'%H:%M').time(),slten=datetime.datetime.strptime("9:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='VEE')
    timetable.objects.create(day='Monday',LT='LT2',sltst=datetime.datetime.strptime("9:00",'%H:%M').time(),slten=datetime.datetime.strptime("10:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='DSY')
    timetable.objects.create(day='Monday',LT='LT2',sltst=datetime.datetime.strptime("11:00",'%H:%M').time(),slten=datetime.datetime.strptime("12:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='DMS')
    timetable.objects.create(day='Monday',LT='LT2',sltst=datetime.datetime.strptime("12:00",'%H:%M').time(),slten=datetime.datetime.strptime("13:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='M2')
    timetable.objects.create(day='Tuesday',LT='LT2',sltst=datetime.datetime.strptime("8:00",'%H:%M').time(),slten=datetime.datetime.strptime("9:30",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='EE&B')
    timetable.objects.create(day='Tuesday',LT='LT2',sltst=datetime.datetime.strptime("9:30",'%H:%M').time(),slten=datetime.datetime.strptime("11:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='DSA')
    timetable.objects.create(day='Wednesday',LT='LT2',sltst=datetime.datetime.strptime("8:00",'%H:%M').time(),slten=datetime.datetime.strptime("9:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='DSY')
    timetable.objects.create(day='Wednesday',LT='LT2',sltst=datetime.datetime.strptime("10:00",'%H:%M').time(),slten=datetime.datetime.strptime("11:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='DMS')
    timetable.objects.create(day='Wednesday',LT='LT2',sltst=datetime.datetime.strptime("11:00",'%H:%M').time(),slten=datetime.datetime.strptime("12:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='M2')
    timetable.objects.create(day='Wednesday',LT='LT2',sltst=datetime.datetime.strptime("12:00",'%H:%M').time(),slten=datetime.datetime.strptime("13:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='VEE')
    timetable.objects.create(day='Thursday',LT='LT2',sltst=datetime.datetime.strptime("8:00",'%H:%M').time(),slten=datetime.datetime.strptime("9:30",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='DSA')
    timetable.objects.create(day='Thursday',LT='LT2',sltst=datetime.datetime.strptime("9:30",'%H:%M').time(),slten=datetime.datetime.strptime("11:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='EE&B')
    timetable.objects.create(day='Friday',LT='LT2',sltst=datetime.datetime.strptime("9:00",'%H:%M').time(),slten=datetime.datetime.strptime("10:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='DMS')
    timetable.objects.create(day='Friday',LT='LT2',sltst=datetime.datetime.strptime("10:00",'%H:%M').time(),slten=datetime.datetime.strptime("11:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='M2')
    timetable.objects.create(day='Friday',LT='LT2',sltst=datetime.datetime.strptime("11:00",'%H:%M').time(),slten=datetime.datetime.strptime("12:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='VEE')
    timetable.objects.create(day='Friday',LT='LT2',sltst=datetime.datetime.strptime("12:00",'%H:%M').time(),slten=datetime.datetime.strptime("13:00",'%H:%M').time(),year='Y18',teacher='Anshu Musaddi',subject='DSY')


if __name__ == '__main__':
    print("updating timetable")
    timetableupd()
    print("updated timetable")
