from django.db import models
from django.contrib.auth.models import User

from apps.usuario.models import Usuario


class Mascota(models.Model):
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    edad = models.IntegerField()
    descripcion = models.TextField()
    especie = models.CharField(max_length=30, null=True)
    color = models.CharField(max_length=30, null=True)
    tamano = models.CharField(max_length=10, null=True)


    # estado = models.BooleanField('Estado', default= True) ELIMINACION LOGICA

    usuario = models.ForeignKey(
        Usuario,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    imagen = models.ImageField(
        max_length=255,
        upload_to='imagen/',
        null=True,
        blank=True,
    )

    # ELIMINACION LOGICA

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.nombre, self.raza, self.genero, self.descripcion)
