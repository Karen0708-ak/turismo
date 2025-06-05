from django.db import models

# Create your models here.
class Lugares(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    resena = models.TextField()
    horario = models.FileField(upload_to='lugares')
    historia = models.FileField(upload_to='lugares')

