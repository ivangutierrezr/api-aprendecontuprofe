from django.db import models

# Create your models here.
class Sesiones(models.Model):
    token = models.CharField(max_length=50)
    idUsuario = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.token