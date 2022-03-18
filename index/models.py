from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField()


class VideoJuegos(models.model):
    vj_nombre = models.CharField(max_length=40)
    vj_genero = models.CharField(max_length=20)
    vj_divertido = models.BooleanField()

class Peliculas(models.Model):
    p_nombre = models.CharField(max_length=30)
    p_categoria = models.CharField(max_length=20)
    p_divertida = models.BooleanField()
    