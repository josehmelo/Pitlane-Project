from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required # Importação necessária

from pilotos.models import Piloto
from .models import Time
from .serializers import TimeSerializer

# --- API VIEWSETS (JSON) ---

class TimeViewSet(viewsets.ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['atividade', 'nacionalidade']
    search_fields = ['nome', 'nome_completo', 'nacionalidade']
    ordering_fields = ['nome', 'campeonatos', 'entrada']

# --- VIEWS PARA FRONTEND (Templates HTML) ---

@login_required(login_url='/login/')
def lista_times_web(request):
    """Lista todas as equipas e os seus pilotos atuais"""
    # Ordenamos por nome para o grid ficar organizado
    equipes = Time.objects.all().order_by('nome')
    return render(request, 'times/list.html', {'equipes': equipes})

@login_required(login_url='/login/')
def detalhe_time_web(request, pk):
    """Mostra detalhes de uma equipa específica e o seu histórico de pilotos"""
    equipe = get_object_or_404(Time, pk=pk)
    
    # Busca os pilotos vinculados a esta equipe
    pilotos = Piloto.objects.filter(equipe=equipe)
    
    return render(request, 'times/detailequipes.html', {
        'equipe': equipe,
        'pilotos': pilotos
    })