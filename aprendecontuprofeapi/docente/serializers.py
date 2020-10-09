from rest_framework import serializers
from .models import Docente

class ListaDocentes(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ('id','nombre','apellidos','numeroIdentificacion')

class NuevoDocente(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ('nombre','apellidos','tipoIdentificacion','numeroIdentificacion','fechaNacimiento','lugarNacimiento','correoElectronco','direccionResidencia','numeroCelular','numeroTelefonoFijo','idInicioSesion','contrasena','urlFotografia')

class CargarDocente(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ('id','nombre','apellidos','tipoIdentificacion','numeroIdentificacion','fechaNacimiento','lugarNacimiento','correoElectronco','direccionResidencia','numeroCelular','numeroTelefonoFijo','idInicioSesion','contrasena','urlFotografia')

class CargarDocenteSesion(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = ('id','idInicioSesion','contrasena')