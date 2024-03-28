from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from travel.serializers import TravelSerializer

from travel.models import Travel

class TravelAPI(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def list(self, request):
        queryset = Travel.objects.all()
        serializer = TravelSerializer(queryset, many=True)
        print("Success")
        return Response(serializer.data)
    
    def create(self, request):
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Success")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Faile")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
