from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from pilotos.models import Piloto
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

def lista_times_web(request):
    """Lista todas as equipas e os seus pilotos atuais"""
    # Usamos o nome do relacionamento reverso (geralmente 'pilotos' ou 'piloto_set')
    equipes = Time.objects.all().order_by('nome')
    return render(request, 'times/list.html', {'equipes': equipes})

def detalhe_time_web(request, pk):
    """Mostra detalhes de uma equipa específica e o seu histórico"""
    equipe = get_object_or_404(Time, pk=pk)
    pilotos = Piloto.objects.filter(equipe=equipe)
    
    return render(request, 'times/detailequipes.html', {
        'equipe': equipe,
        'pilotos': pilotos
    })