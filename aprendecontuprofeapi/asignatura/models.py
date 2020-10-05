from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    grado = models.CharField(max_length=50)
    docente = models.CharField(max_length=50)
    introduccion = models.CharField(max_length=500)
    estudiantes = ArrayField(
        models.CharField(max_length=50)
    )
    talleres = ArrayField(
        models.JSONField(),
        default=list
    )
    evaluaciones = ArrayField(
        models.JSONField(),
        default=list
    )
    respuestasTalleres = ArrayField(
        models.JSONField(),
        default=list
    )
    respuestasEvaluaciones = ArrayField(
        models.JSONField(),
        default=list
    )
    asistencias = ArrayField(
        models.JSONField(),
        default=list
    )
    foro = ArrayField(
        models.JSONField(),
        default=list
    )
