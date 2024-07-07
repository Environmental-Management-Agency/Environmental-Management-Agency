# backend/config/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'data',
    'monitoring',
    'reporting',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'environmental_management_agency',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# backend/apps/data/models.py
from django.db import models

class EnvironmentalData(models.Model):
    parameter = models.CharField(max_length=255)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

# backend/apps/monitoring/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EnvironmentalData

class MonitoringView(APIView):
    def get(self, request):
        data = EnvironmentalData.objects.all()
        return Response({'data': data})

# backend/apps/reporting/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import EnvironmentalData

class ReportingView(APIView):
    def get(self, request):
        data = EnvironmentalData.objects.all()
        return Response({'data': data})
