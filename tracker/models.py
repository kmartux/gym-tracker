from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    nacimiento = models.DateField()
    genero = models.CharField(max_length=100)


class RegistroPeso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)


class Entrenamiento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    duracion = models.IntegerField()
    intensidad = models.IntegerField()
    def __str__(self):
        return f"{self.usuario.username} - {self.fecha}"


class Serie(models.Model):
    entrenamiento = models.ForeignKey(Entrenamiento, on_delete=models.CASCADE)
    ejercicio = models.CharField(max_length=100)
    numero_de_serie = models.IntegerField()
    repeticiones = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    descanso = models.IntegerField()