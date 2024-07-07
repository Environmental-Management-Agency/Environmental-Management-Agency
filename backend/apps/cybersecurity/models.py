# backend/apps/cybersecurity/models.py
from django.db import models

class WasteSystemAlert(models.Model):
    alert_type = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class WasteSystemVulnerability(models.Model):
    vulnerability_type = models.CharField(max_length=255)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
