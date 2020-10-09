from rest_framework import serializers
from .models import Sesiones

class ItemSesion(serializers.ModelSerializer):
    class Meta:
        model = Sesiones
        fields = ('token','rol','idUsuario')