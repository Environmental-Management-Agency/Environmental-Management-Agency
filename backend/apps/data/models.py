# backend/apps/data/models.py
from django.db import models

class WasteManagementData(models.Model):
    parameter = models.CharField(max_length=255)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

# backend/apps/monitoring/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WasteManagementData

class MonitoringView(APIView):
    def get(self, request):
        data = WasteManagementData.objects.all()
        return Response({'data': data})

# backend/apps/reporting/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WasteManagementData

class ReportingView(APIView):
    def get(self, request):
        data = WasteManagementData.objects.all()
        return Response({'data': data})
