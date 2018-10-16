from django.db import models

# Create your models here.
class Chisme(models.Model):
    titulo = models.CharField(max_length=50,blank=True)
    descripcion = models.CharField(max_length=100,blank=True)
    fecha_de_creacion=models.DateTimeField(auto_now_add=True, blank=True)
