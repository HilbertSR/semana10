from django.db import models

# Create your models here.
class Perfil(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    edad = models.IntegerField()
    estatus = models.BooleanField(default=True)