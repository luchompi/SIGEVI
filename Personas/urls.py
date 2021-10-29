from django.urls import path

from . import views as v 

app_name="personas"

urlpatterns = [
    #Urls de Clientes
    path("clientes/", v.ClientesIndex.as_view(), name="clientesIndex"),
    path("clientes/nuevo/", v.ClienteCreate.as_view(), name="clientesNuevos"),
    path("clientes/detalles/<pk>/", v.ClienteDetail.as_view(), name="clientesDetalles"),
    path("clientes/actualizar/<pk>/", v.ClienteUpdate.as_view(), name="clientesActualizar"),
    path("clientes/eliminar/<pk>/", v.ClienteDelete.as_view(), name="clientesEliminar"),

    #urls de Proveedores
    path("proveedores/",v.ProveedorList.as_view(),name="proveedores"),
    path("proveedores/nuevo/",v.ProveedorCreate.as_view(),name="proveedoresNuevos"),
    path("proveedores/detalles/<pk>/",v.ProveedorDetail.as_view(),name="proveedoresDetalles"),
    path("proveedores/actualizar/<pk>/",v.ProveedorUpdate.as_view(),name="proveedoresActualizar"),
    path("proveedores/eliminar/<pk>/",v.ProveedorDelete.as_view(),name="proveedoresEliminar"),




]
