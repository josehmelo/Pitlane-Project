from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PilotoViewSet, PilotoStatusViewSet

router = DefaultRouter()
router.register(r'pilotos', PilotoViewSet, basename='piloto')
router.register(r'pilotos-status', PilotoStatusViewSet, basename='piloto-status')

urlpatterns = router.urls