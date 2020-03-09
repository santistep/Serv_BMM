from django.db import models

from apps.usuario.models import Usuario

# Create your models here.


class Perdido(models.Model):
    raza = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    descripcion = models.TextField()
    fecha_denuncia = models.DateField()
    usuario = models.ForeignKey(
        Usuario,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )