from django.db import models

# Create your models here.


class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    direccion = models.TextField()
    barrio = models.CharField(max_length=20)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellido)
