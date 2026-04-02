from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Piloto, Piloto_Status
from .serializers import PilotoSerializer, PilotoStatusSerializer

class PilotoViewSet(viewsets.ModelViewSet):
    queryset = Piloto.objects.select_related('equipe').all()
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
    
# --- VIEWS PARA FRONTEND (Templates HTML) ---

def lista_pilotos_web(request):
    """Renderiza a página principal com o grid de pilotos"""
    pilotos = Piloto.objects.all().select_related('equipe')
    return render(request, 'pilotos/list.html', {'pilotos': pilotos})

def detalhe_piloto_web(request, pk):
    """Renderiza os detalhes e as estatísticas de um piloto específico"""
    piloto = get_object_or_404(Piloto, pk=pk)
    # Busca o histórico de temporadas desse piloto
    stats = Piloto_Status.objects.filter(piloto=piloto).order_by('-temporada')
    
    context = {
        'piloto': piloto,
        'stats': stats
    }
    return render(request, 'pilotos/detail.html', context)