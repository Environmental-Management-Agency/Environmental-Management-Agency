# backend/apps/telematics/models.py
from django.db import models

class VehicleData(models.Model):
    vehicle_id = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

# backend/apps/telematics/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import VehicleData

class TelematicsView(APIView):
    def get(self, request):
        data = VehicleData.objects.all()
        return Response({'data': data})
