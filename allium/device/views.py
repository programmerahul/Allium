from django.shortcuts import render
from django.http import HttpResponse
from .models import Device
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def index(request):
    if request.method == 'GET':
        device = Device.objects.latest('eventTime')
        res= render(request, 'device.html', {'device': device})
        res['status']=device.status
        return  res
    elif request.method == 'POST':
        json = JSONParser().parse(request)
        device = Device(name=json['name'], temperature=json['temperature'],
                        humidity=json['humidity'], toxicGases=json['toxicGases'],
                        status=json['status'])
        device.save()
        return HttpResponse('Done')


