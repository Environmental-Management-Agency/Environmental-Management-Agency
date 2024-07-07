# backend/apps/iot/models.py
from django.db import models

class WasteSensorData(models.Model):
    sensor_id = models.CharField(max_length=255)
    parameter = models.CharField(max_length=255)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class WasteEdgeDevice(models.Model):
    device_id = models.CharField(max_length=255)
    sensor_data = models.ManyToManyField(WasteSensorData)
