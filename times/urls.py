from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TimeViewSet

router = DefaultRouter()
router.register(r'times', TimeViewSet, basename='time')

urlpatterns = router.urls