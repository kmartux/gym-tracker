from django.shortcuts import render
from rest_framework import generics
from .models import RegistroPeso
from .serializers import RegistroPesoSerializer
# Create your views here.
class RegistroPesoList(generics.ListAPIView):
    queryset = RegistroPeso.objects.all()
    serializer_class = RegistroPesoSerializer