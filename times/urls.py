from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TimeViewSet, lista_times_web, detalhe_time_web

router = DefaultRouter()
router.register(r'times', TimeViewSet, basename='time')

urlpatterns = [
    # Rotas Web (HTML)
    path('web/equipes/', lista_times_web, name='times-lista'),
    path('web/detalheequipes/<int:pk>/', detalhe_time_web, name='time-detalhe'),
    
    # Rotas API (JSON)
    path('', include(router.urls)),
]