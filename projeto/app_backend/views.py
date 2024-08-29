from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from .models import Risco, Solucao, Piloto, Usuario 
from .serializers import RiscoSerializer, SolucaoSerializer

class RiscoListView(viewsets.ModelViewSet):
    queryset = Risco.objects.all()
    serializer_class = RiscoSerializer

class SolucaoListView(viewsets.ModelViewSet):
    queryset = Solucao.objects.all()
    serializer_class = SolucaoSerializer 