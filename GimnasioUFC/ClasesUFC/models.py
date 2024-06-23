from django.db import models

# Create your models here.
class Clase(models.Model):
    nombre=models.CharField(max_length=40)
    tipo=models.CharField(max_length=40)
    #horario=models.TextChoices('am','pm')

class Profesor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    #especialidad=models.TextChoices('boxeo','muaythai','lucha')

class Alumno(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    email=models.EmailField()
    edad=models.IntegerField()
    
    
    
    