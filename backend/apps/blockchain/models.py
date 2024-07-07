# backend/apps/blockchain/models.py
from django.db import models
from hashlib import sha256

class WasteTransaction(models.Model):
    sender = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    hash = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        self.hash = sha256(str(self.sender + self.receiver + str(self.amount) + str(self.timestamp)).encode()).hexdigest()
        super().save(*args, **kwargs)
