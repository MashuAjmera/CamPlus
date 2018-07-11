from django.db import models

# Create your models here.
class menu(models.Model):
    institute = models.CharField(max_length=256)
    day = models.CharField(max_length=256)
    brk = models.CharField(max_length=256)
    lun = models.CharField(max_length=256)
    snk = models.CharField(max_length=256)
    din = models.CharField(max_length=256)

    def __str__(self):
        return self.institute + ' ' + self.day
