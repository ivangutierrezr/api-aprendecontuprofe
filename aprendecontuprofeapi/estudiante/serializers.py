from rest_framework import serializers
from .models import Estudiante

class ListaEstudiantes(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id','nombre','apellidos','numeroIdentificacion')

class NuevoEstudiante(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('nombre','apellidos','tipoIdentificacion','numeroIdentificacion','fechaNacimiento','lugarNacimiento','direccionResidencia','nombreCompletoAcudiente','tipoIdentificaionAcudiente','numeroIdentificacionAcudiente','numeroTelefonicoAcudiente','correoElectroncoAcudiente','idInicioSesion','contrasena','urlFotografia')

class CargarEstudiante(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id','nombre','apellidos','tipoIdentificacion','numeroIdentificacion','fechaNacimiento','lugarNacimiento','direccionResidencia','nombreCompletoAcudiente','tipoIdentificaionAcudiente','numeroIdentificacionAcudiente','numeroTelefonicoAcudiente','correoElectroncoAcudiente','idInicioSesion','contrasena','urlFotografia')

class CargarEstudianteSesion(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id','idInicioSesion','contrasena')