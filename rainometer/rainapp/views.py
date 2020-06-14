from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import volenteer
from .models import raindata
from .serializers import volenteerSerializer
from .serializers import raindataSerializer

class volenteerList(APIView):
    def get(self,request):
        volenteer1=volenteer.objects.all()
        serializer=volenteerSerializer(volenteer1,many=True)
        return Response(serializer.data)

    def post(self):
        pass
class raindataList(APIView):
    def get(self,request):
        raindata1=raindata.objects.all()
        serializer=raindataSerializer(raindata1,many=True)
        return Response(serializer.data)
    def post(self):
        pass