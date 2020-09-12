from django.db import models

# Create your models here.

class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoIdentificacion = models.CharField(max_length=50)
    numeroIdentificacion = models.IntegerField()
    fechaNacimiento = models.DateField()
    lugarNacimiento = models.CharField(max_length=50)
    correoElectronco = models.CharField(max_length=50)
    direccionResidencia = models.CharField(max_length=50)
    numeroCelular = models.IntegerField()
    numeroTelefonoFijo = models.IntegerField()
    idInicioSesion = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    urlFotografia = models.CharField(max_length=50)

