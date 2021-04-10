from django.db import models
from django.contrib.auth.models import User


class Mascota(models.Model):
    nombre = models.CharField(max_length=30)
    especie = models.CharField(max_length=30, null=True)
    raza = models.CharField(max_length=30)
    color = models.CharField(max_length=30, null=True)
    edad = models.IntegerField()
    genero = models.CharField(max_length=10)
    tamaño = models.CharField(max_length=10, null=True)
    recompensa = models.IntegerField(null=True)
    descripcion = models.TextField(null=True)
    ciudad = models.CharField(max_length=30)
    barrio = models.CharField(max_length=30)

    # estado = models.BooleanField('Estado', default= True) ELIMINACION LOGICA

    usuario = models.ForeignKey(
        User,
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
