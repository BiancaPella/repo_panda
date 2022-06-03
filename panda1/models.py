from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

class Alumnos(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()

class Profesores(models.Model):
    profesor = models.CharField(max_length=40)
    materia = models.CharField(max_length=15)
