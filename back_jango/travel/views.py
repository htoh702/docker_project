from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status

from travel.serializers import TravelSerializer

from travel.models import Travel

class TravelAPI(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

# Create your views here.
