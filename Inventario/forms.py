from django import forms
from Gestion.models import Categoria,Marca
from Personas.models import Proveedor
UNIDADES=[
    ('unidad' , "Unidad"),
    ('docena' , "Docena"),
    ('resma' , "Resma"),
    ( 'caja' , "Caja"),
]

class productoForm(forms.Form):
    categoria=forms.ModelChoiceField(queryset=Categoria.objects.all())
    nombre=forms.CharField()
    cantidad=forms.IntegerField()
    uniades = forms.Select(choices=UNIDADES)
    precio_compra = forms.IntegerField()
    proveedor=forms.ModelChoiceField(queryset=Proveedor.objects.all())
    marca=forms.ModelChoiceField(queryset=Marca.objects.all())
