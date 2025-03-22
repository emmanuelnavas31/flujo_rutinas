from django.contrib.auth.models import User
from django.db import models


class Ejercicio(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Rutina(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    time = models.TimeField()
    days = models.CharField(max_length=100)
    exercise = models.ManyToManyField(Ejercicio)

    def __str__(self):
        return f'{self.name} - {self.user.username}'
