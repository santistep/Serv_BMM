from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    direccion = models.CharField(max_length=50)
    barrio = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)
    usuario = models.ForeignKey(
        User,
        null=True,  # False
        blank=True,  # False
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.direccion
