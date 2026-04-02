from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Piloto, Piloto_Status
from .serializers import PilotoSerializer, PilotoStatusSerializer

class PilotoViewSet(viewsets.ModelViewSet):
    queryset = Piloto.objects.select_related('time').all()
    serializer_class = PilotoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['atividade', 'nacionalidade', 'equipe']
    search_fields = ['nome', 'sobrenome', 'codigo', 'nacionalidade']
    ordering_fields = ['sobrenome', 'numero']

class PilotoStatusViewSet(viewsets.ModelViewSet):
    queryset = Piloto_Status.objects.select_related('piloto').all()
    serializer_class = PilotoStatusSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['piloto', 'temporada']
    ordering_fields = ['temporada', 'pontos', 'vitorias', 'posicao']