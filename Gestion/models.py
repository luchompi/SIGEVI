from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50,verbose_name="Digite nombre de Categoría",unique=True, error_messages={'unique':'ya existe esta categoria'})
    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre= models.CharField(max_length=50,verbose_name="Digite nombre de la Marca",unique=True,error_messages={'unique':'Ya existe esta marca en el sistema'})
    def __str__(self):
        return self.nombre

