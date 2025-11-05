from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=255)
    temperature = models.FloatField()
    humidity = models.FloatField()
    toxicGases = models.FloatField()
    status = models.FloatField()
    eventTime = models.DateTimeField(auto_now=True)
