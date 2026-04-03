from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Piloto, Piloto_Status
from .serializers import PilotoSerializer, PilotoStatusSerializer

# Autenticação e Redirecionamento
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages

def cadastro_web(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Faça login agora.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro.html', {'form': form})

# --- API VIEWSETS (Para o JSON/Mobile) ---

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

# --- VIEWS PARA LOGIN/LOGOUT ---

class PitlaneLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('pilotos-lista')

class PitlaneLogoutView(LogoutView):
    next_page = reverse_lazy('login')

# --- VIEWS PARA FRONTEND (Templates HTML) ---

@login_required(login_url='/login/')
def lista_pilotos_web(request):
    ano_selecionado = request.GET.get('ano', '2024')
    
    stats_ano = Piloto_Status.objects.filter(
        temporada=ano_selecionado
    ).select_related('piloto', 'piloto__equipe').order_by('-pontos')

    temporadas_disponiveis = ['2024', '2023', '2022', '2021']

    context = {
        'stats': stats_ano,
        'ano_atual': ano_selecionado,
        'temporadas': temporadas_disponiveis,
    }
    return render(request, 'pilotos/list.html', context)

@login_required(login_url='/login/')
def detalhe_piloto_web(request, pk):
    """Renderiza os detalhes e as estatísticas de um piloto específico"""
    piloto = get_object_or_404(Piloto, pk=pk)
    stats = Piloto_Status.objects.filter(piloto=piloto).order_by('-temporada')
    
    context = {
        'piloto': piloto,
        'stats': stats
    }
    return render(request, 'pilotos/detail.html', context)