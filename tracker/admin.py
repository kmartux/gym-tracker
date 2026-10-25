from django.contrib import admin
from .models import Perfil, RegistroPeso, Entrenamiento,Serie
# register your models here.
admin.site.register(Perfil)
admin.site.register(RegistroPeso)
admin.site.register(Entrenamiento)
admin.site.register(Serie)