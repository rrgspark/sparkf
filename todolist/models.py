from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    descripcion = models.CharField(max_length=255)
    completado = models.BooleanField(default=False)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
