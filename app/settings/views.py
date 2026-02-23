from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app.settings.models import Settings
from app.settings.serializers import SettingsSerializer

class HelloAPIView(APIView):
    def get(self, request):
        return Response({"message" : "Hello DRF!"})

class SettingsListAPIView(APIView):
    def get(self, request):
        settings = Settings.objects.all()
        serializer = SettingsSerializer(settings, many=True)
        return Response(serializer.data)

class SettingsCreateAPIView(APIView):
    def post(self, request):
        serializer = SettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)