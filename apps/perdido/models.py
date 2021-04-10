from datetime import date

from django.db import models
from apps.mascota.models import Mascota

# Create your models here.


class Perdido(models.Model):

    fecha_denuncia = models.DateField(default=date.today)

    descripcion = models.TextField()

    ciudad = models.CharField(max_length=30)

    barrio = models.CharField(max_length=30)

    contacto = models.CharField(max_length=60, null=False, blank=False)

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

    class Meta:

        ordering = ['ciudad','barrio']