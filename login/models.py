from django.db import models

class Usuario(models.Model):
    Nombre = models.CharField(max_length=100)
    ApellidoP = models.CharField(max_length=100)
    ApellidoM = models.CharField(max_length=100)
    Correo = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)