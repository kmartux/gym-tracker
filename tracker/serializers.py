from rest_framework import serializers
from .models import RegistroPeso


class RegistroPesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroPeso
        fields = ['id', 'peso', 'fecha']