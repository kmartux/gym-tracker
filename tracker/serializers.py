from rest_framework import serializers
from .models import RegistroPeso, Entrenamiento
##Sirve para traducir entre tu base de datos y el JSON que entiende React.

class RegistroPesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPeso
        fields = ['id', 'peso', 'fecha']

class EntrenamientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenamiento
        fields = ['id', 'fecha', 'duracion', 'intensidad']