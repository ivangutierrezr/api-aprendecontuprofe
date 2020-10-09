from django.db import models

# Create your models here.

class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoIdentificacion = models.CharField(max_length=50)
    numeroIdentificacion = models.CharField(max_length=50)
    fechaNacimiento = models.CharField(max_length=50, blank=True)
    lugarNacimiento = models.CharField(max_length=50)
    correoElectronco = models.CharField(max_length=50, blank=True)
    direccionResidencia = models.CharField(max_length=50, blank=True)
    numeroCelular = models.CharField(max_length=50)
    numeroTelefonoFijo = models.CharField(max_length=50, blank=True)
    idInicioSesion = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    urlFotografia = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

