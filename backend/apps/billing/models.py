# backend/apps/billing/models.py
from django.db import models

class WasteBinData(models.Model):
    bin_id = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

# backend/apps/billing/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WasteBinData

class BillingView(APIView):
    def get(self, request):
        data = WasteBinData.objects.all()
        return Response({'data': data})
