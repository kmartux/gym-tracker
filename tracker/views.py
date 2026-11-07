from django.shortcuts import render
from rest_framework import generics
from .models import RegistroPeso, Entrenamiento,Serie
from .serializers import RegistroPesoSerializer, EntrenamientoSerializer,SerieSerializer
# Create your views here.
class RegistroPesoList(generics.ListCreateAPIView):
    serializer_class = RegistroPesoSerializer
    
    def get_queryset(self):
        return RegistroPeso.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class EntrenamientoList(generics.ListCreateAPIView):
    serializer_class = EntrenamientoSerializer

    def get_queryset(self):
        return Entrenamiento.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class SerieList(generics.ListCreateAPIView):
    serializer_class = SerieSerializer

    def get_queryset(self):
        return Serie.objects.filter(entrenamiento__usuario=self.request.user)