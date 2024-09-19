from django.shortcuts import render
from rest_framework import viewsets,filters,status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializer import tareasSerializer
from.models import tareas
# Create your views here.

class tareasView(viewsets.ModelViewSet):
    serializer_class=tareasSerializer
    queryset=tareas.objects.all()
    
    