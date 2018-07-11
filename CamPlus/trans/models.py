from django.db import models

# Create your models here.
class buswd(models.Model):
    institute = models.CharField(max_length=256)
    frm = models.CharField(max_length=256)
    to = models.CharField(max_length=256)
    time = models.TimeField()
    busno = models.IntegerField(null=True)
    operator = models.CharField(max_length=256)
    def __str__(self):
        return self.institute + ' ' + self.time

class buswe(models.Model):
    institute = models.CharField(max_length=256)
    frm = models.CharField(max_length=256)
    to = models.CharField(max_length=256)
    time = models.TimeField()
    busno = models.IntegerField(null=True)
    operator = models.CharField(max_length=256)
    def __str__(self):
        return self.institute + ' ' + self.time
