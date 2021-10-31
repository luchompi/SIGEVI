from django.shortcuts import redirect, render
from django.utils.datetime_safe import datetime
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from Gestion.models import Categoria
from carrito.carrito import Carrito
from .forms import productoForm
from .models import Producto

#Reportlab dependences
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4
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


def ProductoCategoria(request,categoria):
    query = Categoria.objects.get(nombre=categoria)
    query1 = Producto.objects.filter(categoria__id=query.pk)
    return render(request,'Producto/related.html',context={'query1':query1})



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

def pagar(request):
    carrito = Carrito(request)
    response = HttpResponse(content_type='Application/pdf')
    d = datetime.today().strftime('%d-%m-%Y')
    response['Content-Disposition']=f'inline; filename="{d}.pdf"'
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    c_compra = request.session["carrito"]
    ide = []
    nombre = []
    cantidad = []
    valor = []
    p_unitario = []
    aux=0
    aux1 =0
    total =0
    for row in c_compra.keys():
            ide.append(c_compra[row]["producto_id"])
            nombre.append(c_compra[row]["nombre"])
            aux1 =c_compra[row]["cantidad"]
            cantidad.append(str(aux1))
            aux = c_compra[row]["acmuluado"]
            valor.append(str(aux))
            p_unitario.append(str(c_compra[row]["unitario"]))

    p.setFont("Helvetica",15,leading=None)
    p.setFillColorRGB(0.29296875,0.453125,0.609375)
    p.drawString(260,800,"Papeleria Y Variedades Dangedav")
    p.line(0,780,1000,780)
    p.line(0,780,1000,778)
    p.drawString(200,750,"FACTURA DE COMPRA")
    #render
    p.setFont("Helvetica",10,leading=None)
    p.drawString(50,690,"Producto ") 
    x =670
    for elemento in nombre:
        p.drawString(50,x,elemento)
        x = x -10

    x =670
    p.drawString(250,690,"Precio Unitario ") 
    for elemento in p_unitario:
        p.drawString(250,x,elemento)
        x = x -10
    x =670
    p.drawString(350,690,"Cantidad") 
    for elemento in cantidad:
        p.drawString(350,x,elemento)
        x = x -10
    x =670
    p.drawString(450,690,"Subtotal") 
    for elemento in valor:
        p.drawString(450,x,elemento)
        x = x -10  
    for key, value in request.session["carrito"].items():
        total += int(value["acmuluado"])
    p.setFont("Helvetica",15,leading=None)
    p.drawString(50,50,"Total")
    p.drawString(400,50,"$") 
    p.drawString(415,50,str(total))
    p.setTitle(f'Report on {d}')
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    carrito.pay()
    return response

def generar_pdf(request):
    response = HttpResponse(content_type='Application/pdf')
    d = datetime.today().strftime('%d-%m-%Y')
    response['Content-Disposition']=f'inline; filename="{d}.pdf"'
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    c_compra = request.session["carrito"]
    ide = []
    nombre = []
    cantidad = []
    valor = []
    p_unitario = []
    aux=0
    aux1 =0
    total =0
    for row in c_compra.keys():
            ide.append(c_compra[row]["producto_id"])
            nombre.append(c_compra[row]["nombre"])
            aux1 =c_compra[row]["cantidad"]
            cantidad.append(str(aux1))
            aux = c_compra[row]["acmuluado"]
            valor.append(str(aux))
            p_unitario.append(str(c_compra[row]["unitario"]))

    p.setFont("Helvetica",15,leading=None)
    p.setFillColorRGB(0.29296875,0.453125,0.609375)
    p.drawString(260,800,"Papeleria Y Variedades Dangedav")
    p.line(0,780,1000,780)
    p.line(0,780,1000,778)
    p.drawString(200,750,"FACTURA DE COMPRA")
    #render
    p.setFont("Helvetica",10,leading=None)
    p.drawString(50,690,"Producto ") 
    x =670
    for elemento in nombre:
        p.drawString(50,x,elemento)
        x = x -10

    x =670
    p.drawString(250,690,"Precio Unitario ") 
    for elemento in p_unitario:
        p.drawString(250,x,elemento)
        x = x -10
    x =670
    p.drawString(350,690,"Cantidad") 
    for elemento in cantidad:
        p.drawString(350,x,elemento)
        x = x -10
    x =670
    p.drawString(450,690,"Subtotal") 
    for elemento in valor:
        p.drawString(450,x,elemento)
        x = x -10  
    for key, value in request.session["carrito"].items():
        total += int(value["acmuluado"])
    p.setFont("Helvetica",15,leading=None)
    p.drawString(50,50,"Total")
    p.drawString(400,50,"$") 
    p.drawString(415,50,str(total))
    p.setTitle(f'Report on {d}')
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response