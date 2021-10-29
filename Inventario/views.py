from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from Gestion.models import Categoria
from carrito.carrito import Carrito
from .forms import productoForm
from .models import Producto

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
    template_name = "Producto/update.html"
    success_url= '/inventario/producto/detalles/{id}/'

class ProductoDetail(DetailView):
    model = Producto
    template_name = "Producto/details.html"


class ProductoDelete(DeleteView):
    model = Producto
    template_name = "Producto/delete.html"
    success_url= '/inventario/producto/'


def agregar_carrito(request,pk):
    producto = Producto.objects.get(id=pk)
    carrito = Carrito(request)
    carrito.add(producto)
    return redirect('/inventario/producto/')

def eliminar_producto(request,pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=pk)
    carrito.remove(producto)
    return redirect("Inventario:productoIndex")

def restar_producto(request,pk):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=pk)
    carrito.decrement(producto)
    return redirect('/inventario/producto/')

def limpiar(request):
    carrito = Carrito(request)
    carrito.clear()
    return redirect("/inventario/producto/")
