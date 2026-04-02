from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Time
from .serializers import TimeSerializer
# Create your views here.

class TimeViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['atividade', 'nacionalidade']
    search_fields = ['nome', 'nome_completo', 'nacionalidade']
    ordering_fields = ['nome', 'campeonatos', 'entrada']
