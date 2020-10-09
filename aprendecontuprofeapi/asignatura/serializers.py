from rest_framework import serializers
from .models import Asignatura

class ListaAsignaturas(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('id','nombre','grado','docente')

class NuevaAsignatura(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('nombre','grado','docente','introduccion','estudiantes', 'clases','talleres','evaluaciones','respuestasTalleres','respuestasEvaluaciones','asistencias','foro')

class CargarAsignatura(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('id','nombre','grado','docente','introduccion','estudiantes', 'clases', 'talleres','evaluaciones','respuestasTalleres','respuestasEvaluaciones','asistencias','foro')