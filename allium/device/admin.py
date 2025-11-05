from django.contrib import admin
from . models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'temperature', 'humidity',
                    'toxicGases', 'status', 'eventTime')


admin.site.register(Device, DeviceAdmin)
