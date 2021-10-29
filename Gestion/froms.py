from django import forms

class marcaForm(forms.Form):
    nombre=forms.CharField()

class categoriaForm(forms.Form):
    nombre = forms.CharField()
