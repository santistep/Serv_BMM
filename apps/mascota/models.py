from django.db import models

from apps.usuario.models import Usuario

# Create your models here.


class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    descripcion = models.TextField()
    usuario = models.ForeignKey(
        Usuario,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )


