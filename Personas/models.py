from django.db import models

# Create your models here.
class Cliente(models.Model):
    identificacion=models.CharField(max_length=50,verbose_name="Identificacion",primary_key=True)
    nombre=models.CharField(max_length=50,verbose_name="Digite Nombre")
    apellido=models.CharField(max_length=50,verbose_name="Digite Apellidos")
    direccion=models.CharField(max_length=100,verbose_name="Digite Dirección de cliente")
    telefono=models.CharField(max_length=50,verbose_name="Digite Teléfono de contacto",null=True,blank=True)
    correo=models.EmailField(null=True,blank=True)
    esFrecuente=models.BooleanField(default=False)
    
    def __str__(self):
        return '%s %s %s'%(self.identificacion,self.nombre,self.apellido)

class Proveedor(models.Model):
    NIT=models.CharField(max_length=50,verbose_name="NIT/C.C.",primary_key=True)
    razonSocial=models.CharField(max_length=50,verbose_name="Nombre de Empresa o Proveedor",unique=True,error_messages={'unique':'Ya existe esta empresa con otro NIT'})
    direccionEmpresa=models.CharField(max_length=50,verbose_name="Dirección de contacto")
    direccionVenta=models.CharField(max_length=50,verbose_name="Dirección de punto de venta",null=True,blank=True)
    telefono=models.CharField(max_length=30, verbose_name="Telefono de contacto",null=True,blank=True)
    correo=models.CharField(max_length=250,verbose_name="Correo electrónico de contacto",null=True,blank=True)

    def __str__(self):
        return '%s %s'%(self.NIT,self.razonSocial)