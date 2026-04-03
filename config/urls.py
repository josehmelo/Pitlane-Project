"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
# Importações com PascalCase (Letras Maiúsculas)
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from pilotos.views import PitlaneLoginView, PitlaneLogoutView, cadastro_web

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', PitlaneLoginView.as_view(), name='login'),
    path('logout/', PitlaneLogoutView.as_view(), name='logout'),
    path('cadastro/', cadastro_web, name='cadastro'),
    
    # JWT - Autenticação (Ajustado para bater com o Import acima)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Apps
    path('api/', include('times.urls')),
    path('api/', include('pilotos.urls')),
    
    # Swagger - Documentação automática
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]