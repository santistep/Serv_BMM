from datetime import date

from django.db import models
from apps.mascota.models import Mascota


# Create your models here.


class Perdido(models.Model):
    fecha_denuncia = models.DateTimeField(null=True)

    recompensa = models.IntegerField(null=True)

    ultima_posicion_conocida = models.CharField(max_length=60, null=True)

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
    )

    imagen = models.ImageField(
        max_length=255,
        upload_to='imagen/',
        null=True,
        blank=True,
    )


