from django.db import models

from Inventario.models import Producto

# Create your models here.
class Carrito(models.Model):
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=10)
    total =  models.CharField(max_length=10)