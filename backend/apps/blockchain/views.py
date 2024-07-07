# backend/apps/blockchain/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WasteTransaction

class BlockchainView(APIView):
    def get(self, request):
        transactions = WasteTransaction.objects.all()
        return Response({'transactions': transactions})

    def post(self, request):
        transaction = WasteTransaction(
            sender=request.data['sender'],
            receiver=request.data['receiver'],
            amount=request.data['amount']
        )
        transaction.save()
        return Response({'transaction': transaction})
