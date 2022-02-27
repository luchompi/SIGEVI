from django.shortcuts import render
from .models import Cliente,Proveedor
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .forms import clienteForm, proveedorForm

#Procedimientos de Clientes
class ClientesIndex(ListView):
    model = Cliente
    template_name = "Personas/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('identificacion'):
            context["query"] = Cliente.objects.filter(identificacion__istartswith=consulta)
        else:
            context["query"] = Cliente.objects.all()
        return context

class ClienteCreate(CreateView):
    model = Cliente
    form = clienteForm
    fields =[
        'identificacion',
        'nombre',
        'apellido',
        'direccion',
        'telefono',
        'correo',
    ]
    template_name = "Personas/create.html"
    success_url = '/personas/clientes/'

class ClienteDetail(DetailView):
    model = Cliente
    template_name = "Personas/details.html"

class ClienteUpdate(UpdateView):
    model = Cliente
    form = clienteForm
    fields =[
        'nombre',
        'apellido',
        'direccion',
        'telefono',
        'correo',
    ]
    template_name = "Personas/update.html"
    success_url = "/personas/clientes/detalles/{identificacion}"

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "Personas/delete.html"
    success_url= "/personas/clientes/"


#procedimientos de Proveedores

class ProveedorList(ListView):
    model = Proveedor
    template_name = "Proveedor/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if consulta := self.request.GET.get('NIT'):
            context["query"] = Proveedor.objects.filter(NIT__istartswith=consulta)
        else:
            context["query"] = Proveedor.objects.all()
        return context
    

class ProveedorCreate(CreateView):
    model = Proveedor
    form = proveedorForm
    fields =[

            'NIT',
            'razonSocial',
            'direccionEmpresa',
            'direccionVenta',
            'telefono',
            'correo',
    ]
    template_name = "Proveedor/create.html"
    success_url = '/personas/proveedores/'


class ProveedorDetail(DetailView):
    model = Proveedor
    template_name = "Proveedor/details.html"


class ProveedorUpdate(UpdateView):
    model = Proveedor
    form = proveedorForm
    fields =[
            'razonSocial',
            'direccionEmpresa',
            'direccionVenta',
            'telefono',
            'correo',
    ]
    template_name = "Proveedor/update.html"
    success_url = '/personas/proveedores/detalles/{NIT}/'


class ProveedorDelete(DeleteView):
    model = Proveedor
    template_name = "Proveedor/delete.html"
    success_url = '/personas/proveedores/'
