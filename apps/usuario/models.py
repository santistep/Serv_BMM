from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    email = models.EmailField(max_length=30, primary_key=True , default="no@mail")
    contrasena = models.CharField(max_length=30, null=True)
    nombre_usuario = models.CharField(max_length=30, null=True)
    telefono = models.CharField(max_length=9, null=True)

    direccion = models.CharField(max_length=50)
    barrio = models.CharField(max_length=20)
    usuario = models.ForeignKey(
        User,
        null=True,  # False
        blank=True,  # False
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.direccion
