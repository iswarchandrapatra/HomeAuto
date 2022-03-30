from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Device,UserDevice

# Create your views here.
def index(request):
    return HttpResponse("this is home__u r not Welcome")

def getdevicestatus(request,pk):
    try:
        device=Device.objects.get(deviceId=pk)
        dict_={"deviceId":device.deviceId,
        "light":device.lightstatus,
        "fan":device.fanstatus}
        
        return JsonResponse(dict_)
    except Device.DoesNotExist:

        return JsonResponse({"message":"no device found"})


def togglelight(request,pk):
        try:
            device=Device.objects.get(deviceId=pk)

            if device.lightstatus==0:
                device.lightstatus=1
            else:
                device.lightstatus=0

            device.save()
            dict_={"deviceId":device.deviceId,
                    "light":device.lightstatus,
                    "fan":device.fanstatus}
            return JsonResponse(dict_)
        except Device.DoesNotExist:

            return JsonResponse({"message":"no device found"})


def togglefan(request,pk):
        try:
            device=Device.objects.get(deviceId=pk)

            if device.fanstatus==0:
                device.fanstatus=1
            else:
                device.fanstatus=0
            device.save()
            dict_={"deviceId":device.deviceId,
                    "light":device.lightstatus,
                    "fan":device.fanstatus}
            return JsonResponse(dict_)
        

        except Device.DoesNotExist:

            return JsonResponse({"message":"no device found"})