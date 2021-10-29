from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView

from Gestion.models import Categoria
from .models import Producto
from .forms import productoForm
# Create your views here.

#Gestion de Productos
class ProductoList(ListView):
    model = Producto
    template_name = "Producto/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        consulta = self.request.GET.get('producto')
        if consulta:
            context["query"] = Producto.objects.filter(nombre__istartswith=consulta)
        else:
            context["query"] = Producto.objects.all()
        return context
    

class ProductoCreate(CreateView):
    model = Producto
    forms = productoForm
    fields=[
        'categoria',
        'nombre',
        'cantidad',
        'uniades',
        'precio_compra',
        'proveedor',
        'marca',
    ]
    template_name = "Producto/create.html"
    success_url= '/inventario/producto/'

class ProductoUpdate(UpdateView):
    model = Producto
    forms = productoForm
    fields=[
        'categoria',
        'nombre',
        'cantidad',
        'uniades',
        'precio_compra',
        'proveedor',
        'marca',
    ]
    template_name = "Producto/create.html"
    success_url= '/inventario/producto/detalles/{id}/'

class ProductoDetail(DetailView):
    model = Producto
    template_name = "Producto/details.html"


class ProductoDelete(DeleteView):
    model = Producto
    template_name = "Producto/delete.html"
    success_url= '/inventario/producto/'
