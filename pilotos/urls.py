from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PilotoViewSet, PilotoStatusViewSet, detalhe_piloto_web, lista_pilotos_web

router = DefaultRouter()
router.register(r'pilotos', PilotoViewSet, basename='piloto')
router.register(r'pilotos-status', PilotoStatusViewSet, basename='piloto-status')

urlpatterns = [
    # Inclui as rotas do DRF (api/pilotos/, api/pilotos-status/)
    path('', include(router.urls)),
    
    # Rotas de Template HTML (Frontend)
    # Acessíveis via api/web/lista/ ou conforme o prefixo no config/urls.py
    path('web/pilotos/', lista_pilotos_web, name='pilotos-lista'),
    path('web/detalhepilotos/<int:pk>/', detalhe_piloto_web, name='piloto-detalhe'),
]