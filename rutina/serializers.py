from django.contrib.auth.models import User
from rest_framework import serializers

from rutina.models import Ejercicio, Rutina


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = '__all__'


class RutinaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    ejercicios = EjercicioSerializer(many=True, read_only=True)
    ejercicios_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ejercicio.objects.all(), write_only=True, source='Ejercicios'
    )

    class Meta:
        model = Rutina
        fields = ['id', 'usuario', 'nombre', 'hora', 'dias', 'ejercicios', 'ejercicios_ids']
