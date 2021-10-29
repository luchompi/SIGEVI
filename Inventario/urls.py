from django.urls import path 
from . import views as v
app_name="Inventario"
urlpatterns = [
    


    #Gestion de Productos
    path('producto/',v.ProductoList.as_view(),name="productoIndex"),
    path('producto/nuevo/',v.ProductoCreate.as_view(),name="productoCrear"),
    path('producto/detalles/<pk>/',v.ProductoDetail.as_view(),name="productoDetalle"),
    path('producto/actualizar/<pk>/',v.ProductoUpdate.as_view(),name="productoEditar"),
    path('producto/eliminar/<pk>/',v.ProductoDelete.as_view(),name="productoEliminar"),

    #carrito
    path('agregar/<pk>/',v.agregar_carrito,name="add"),
    path('eliminar/<pk>/',v.eliminar_producto,name="del"),
    path('restar/<pk>/',v.restar_producto,name="remove"),
    path('limpiar/',v.limpiar,name="cls"),




]
