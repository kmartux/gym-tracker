from django.shortcuts import render
from rest_framework import generics
from .models import RegistroPeso, Entrenamiento
from .serializers import RegistroPesoSerializer, EntrenamientoSerializer
# Create your views here.
class RegistroPesoList(generics.ListAPIView):
    queryset = RegistroPeso.objects.all()
    serializer_class = RegistroPesoSerializer

class EntrenamientoList(generics.ListAPIView):
    queryset = Entrenamiento.objects.all()
    serializer_class = EntrenamientoSerializer

