from django.shortcuts import render
from Gestion.froms import marcaForm,categoriaForm
from Inventario.views import ProductoDetail
from .models import Marca,Categoria
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from Inventario.models import Producto
# Create your views here.


class MarcaList(ListView):
    model = Marca
    template_name = "Marca/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('marca'):
            context["query"] = Marca.objects.filter(nombre__istartswith=consulta)
        else:
            context["query"]= Marca.objects.all()
        return context
    

class MarcaCreate(CreateView):
    model = Marca
    form = marcaForm
    fields=['nombre',]
    template_name = "Marca/create.html"
    success_url = '/gestion/marcas/'


class MarcaUpdate(UpdateView):
    model = Marca
    template_name = "Marca/update.html"
    form = marcaForm
    fields=['nombre',]
    success_url = '/gestion/marcas/'


class MarcaDelete(DeleteView):
    model = Marca
    template_name = "Marca/delete.html"
    success_url = '/gestion/marcas/'
    def get_context_data(self, **kwargs):
        query= Marca.objects.get(nombre=self.object)
        context = super().get_context_data(**kwargs)
        context["query1"] = Producto.objects.filter(marca__id=query.id)
        return context
    
    


class CategoriaList(ListView):
    model = Categoria
    template_name = "Categoria/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('categoria'):
            context["query"] = Categoria.objects.filter(nombre__istartswith=consulta)
        else:
            context["query"] = Categoria.objects.all()
        return context
    

class CategoriaCreate(CreateView):
    model = Categoria
    form = categoriaForm
    fields=['nombre',]
    template_name = "Categoria/create.html"
    success_url = '/gestion/categoria/'


class CategoriaUpdate(UpdateView):
    model = Categoria
    form = categoriaForm
    fields=['nombre',]
    template_name = "Categoria/update.html"
    success_url = '/gestion/categoria/'



def CategoriaDetail(request,pk):
    query = Categoria.objects.get(id=pk)
    query1 = Producto.objects.filter(categoria__id=pk)
    if not query:
        query = Categoria.objects.get(nombre=query1)
    return render(request,'Categoria/details.html',context={'query':query,'query1':query1})



    
    

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = "Categoria/delete.html"
    success_url = '/gestion/categoria/'

