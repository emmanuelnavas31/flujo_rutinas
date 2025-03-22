from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RutinaViewSet, EjerciciosViewSet

router = DefaultRouter()
router.register(r'rutinas', RutinaViewSet, basename='rutina')
router.register(r'ejercicios', EjerciciosViewSet, basename='ejercicio')

urlpatterns = [
    path('', include(router.urls)),
]
