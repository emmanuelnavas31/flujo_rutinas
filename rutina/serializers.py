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
    user = UserSerializer(read_only=True)
    exercise = EjercicioSerializer(many=True, read_only=True)

    exercise_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ejercicio.objects.all(), write_only=True, source='exercise'
    )

    class Meta:
        model = Rutina
        fields = ['id', 'user', 'name', 'time', 'days', 'exercise', 'exercise_ids']

    def create(self, validated_data):
        exercises = validated_data.pop('exercise', [])
        user = self.context['request'].user
        rutina = Rutina.objects.create(user=user, **validated_data)
        rutina.exercise.set(exercises)
        return rutina