from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoIdentificacion = models.CharField(max_length=50)
    numeroIdentificacion = models.IntegerField()
    fechaNacimiento = models.DateField()
    lugarNacimiento = models.CharField(max_length=50)
    direccionResidencia = models.CharField(max_length=50)
    nombreCompletoAcudiente = models.CharField(max_length=50)
    tipoIdentificaionAcudiente = models.CharField(max_length=50)
    numeroIdentificacionAcudiente = models.IntegerField()
    numeroTelefonicoAcudiente = models.IntegerField()
    correoElectroncoAcudiente = models.CharField(max_length=50)
    idInicioSesion = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    urlFotografia = models.CharField(max_length=50)
