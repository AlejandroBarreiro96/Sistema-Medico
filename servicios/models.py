from django.db import models

class Servicio(models.Model):
    tuitulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField()
    created=models.DateField(auto_created=True)
    updated=models.DateField(auto_created=True)
    class meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.titulo 



