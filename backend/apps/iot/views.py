# backend/apps/iot/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import WasteSensorData, WasteEdgeDevice

class IoTView(APIView):
    def get(self, request):
        devices = WasteEdgeDevice.objects.all()
        return Response({'devices': devices})

    def post(self, request):
        device = WasteEdgeDevice(device_id=request.data['device_id'])
        device.save()
        sensor_data = WasteSensorData(
            sensor_id=request.data['sensor_id'],
            parameter=request.data['parameter'],
            value=request.data['value']
        )
        sensor_data.save()
        device.sensor_data.add(sensor_data)
        return Response({'device': device})
