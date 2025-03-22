from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from rutina.models import Ejercicio, Rutina
from rutina.serializers import EjercicioSerializer, RutinaSerializer


class EjerciciosViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer
    permission_classes = [IsAuthenticated]


class RutinaViewSet(viewsets.ModelViewSet):
    serializer_class = RutinaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Rutina.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
