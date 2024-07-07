# backend/apps/cybersecurity/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WasteSystemAlert, WasteSystemVulnerability

class CybersecurityView(APIView):
    def get(self, request):
        alerts = WasteSystemAlert.objects.all()
        vulnerabilities = WasteSystemVulnerability.objects.all()
        return Response({'alerts': alerts, 'vulnerabilities': vulnerabilities})

    def post(self, request):
        alert = WasteSystemAlert(
            alert_type=request.data['alert_type'],
            description=request.data['description']
        )
alert.save()
        return Response({'alert': alert})
