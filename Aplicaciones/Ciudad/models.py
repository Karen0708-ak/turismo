from django.db import models

# Create your models here.
class Ciudad(models.Model):
    CLIMA_CHOICES = [
        ('templado', 'Templado'),
        ('tropical', 'Tropical'),
    ]
    nombre = models.CharField(max_length=100)
    clima = models.CharField(max_length=10, choices=CLIMA_CHOICES)
    poblacion = models.IntegerField()
    foto = models.FileField(upload_to ='docu',null=True, blank=True)
    folleto = models.FileField(upload_to='docu',null=True, blank=True)
