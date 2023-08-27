from django.db import models
from django.db import models
class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=8)
    correoelectronico = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=20) 

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.PositiveIntegerField()
    localidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

class Carrera(models.Model):
    usuario = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
