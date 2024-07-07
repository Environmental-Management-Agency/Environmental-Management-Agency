# backend/apps/robotics/models.py
from django.db import models

class RoboticSorterData(models.Model):
    sorter_id = models.CharField(max_length=255)
    material_composition = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

# backend/apps/robotics/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RoboticSorterData

class RoboticsView(APIView):
    def get(self, request):
        data = RoboticSorterData.objects.all()
        return Response({'data': data})
