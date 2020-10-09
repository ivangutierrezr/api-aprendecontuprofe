from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
class Asignatura(models.Model):
    nombre = models.CharField(max_length=50)
    grado = models.CharField(max_length=50)
    docente = models.CharField(max_length=50)
    introduccion = models.CharField(max_length=500, blank=True)
    estudiantes = ArrayField(
        models.CharField(max_length=50),
        blank=True
    )
    clases = ArrayField(
        models.JSONField(),
        blank=True,
        default=list
    )
    talleres = ArrayField(
        models.JSONField(),
        blank=True,
        default=list
    )
    evaluaciones = ArrayField(
        models.JSONField(),
        blank=True,
        default=list
    )
    respuestasTalleres = ArrayField(
        models.JSONField(),
        blank=True,
        default=list
    )
    respuestasEvaluaciones = ArrayField(
        models.JSONField(),
        blank=True,
        default=list
    )
    asistencias = ArrayField(
        models.JSONField(),
        blank=True,
        default=list
    )
    foro = ArrayField(
        models.JSONField(),
        blank=True,
        default=list
    )

    def __str__(self):
        return self.nombre
