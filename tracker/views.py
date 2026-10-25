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

class EntrenamientoList(generics.ListAPIView):
    queryset = Entrenamiento.objects.all()
    serializer_class = EntrenamientoSerializer

class SerieList(generics.ListAPIView):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer
