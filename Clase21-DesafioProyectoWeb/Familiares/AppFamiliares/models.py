import email
from django.db import models

# Create your models here.

class Familiares(models.Model):
    
    tipo = models.CharField(max_length= 30)
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    fecha_nacimiento = models.DateField()
    edad = models.IntegerField()

class Amigos(models.Model):
    
    nombre = models.CharField(max_length= 50)
    apellido = models.CharField(max_length= 50)
    email = models.EmailField(max_length=50)
    Nacionalidad = models.CharField(max_length= 50)
    edad = models.IntegerField()

class Mascotas(models.Model):
    
    nombre = models.CharField(max_length= 50)
    Tipo = models.CharField(max_length= 30)
 