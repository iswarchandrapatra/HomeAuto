from os import device_encoding
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Device(models.Model):
    deviceId=models.CharField(max_length=10,primary_key=True)
    deviceType=models.CharField(max_length=20)
    lightstatus=models.IntegerField(choices=((0,0),(1,1)),default=0)
    fanstatus=models.IntegerField(choices=((0,0),(1,1)),default=0)


    def __str__(self):
        return self.deviceId


class UserDevice(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)


    def __str__(self):
        return self.user + self.device

    