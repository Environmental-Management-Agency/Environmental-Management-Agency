# backend/apps/ai/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WasteClassificationModel

class AIView(APIView):
    def get(self, request):
        model = WasteClassificationModel.objects.last()
        return Response({'accuracy': model.accuracy})

    def post(self, request):
        model = WasteClassificationModel()
        model.train_model()
        return Response({'accuracy': model.accuracy})
