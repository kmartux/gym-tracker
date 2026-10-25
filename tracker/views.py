from django.shortcuts import render
from rest_framework import generics
from .models import RegistroPeso, Entrenamiento,Serie
from .serializers import RegistroPesoSerializer, EntrenamientoSerializer,SerieSerializer
# Create your views here.
class RegistroPesoList(generics.ListCreateAPIView):
    queryset = RegistroPeso.objects.all()
    serializer_class = RegistroPesoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class EntrenamientoList(generics.ListCreateAPIView):
    queryset = Entrenamiento.objects.all()
    serializer_class = EntrenamientoSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class SerieList(generics.ListCreateAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer