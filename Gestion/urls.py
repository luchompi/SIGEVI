from django.urls import path
from . import views as v
app_name="gestion"

urlpatterns = [
    #Gestion de Marcas
    path('marcas/',v.MarcaList.as_view(),name="marcaIndex"),
    path('marcas/nuevo/',v.MarcaCreate.as_view(),name="marcaCrear"),
    path('marcas/actualizar/<pk>/',v.MarcaUpdate.as_view(),name="marcaActualizar"),
    path('marcas/eliminar/<pk>/',v.MarcaDelete.as_view(),name="marcaEliminar"),
     
     #Gestion de Categorías
    path('categoria/',v.CategoriaList.as_view(),name="categoriaIndex"),
    path('categoria/nuevo/',v.CategoriaCreate.as_view(),name="categoriaCrear"),
    path('categoria/actualizar/<pk>/',v.CategoriaUpdate.as_view(),name="categoriaEditar"),
    path('categoria/eliminar/<pk>/',v.CategoriaDelete.as_view(),name="categoriaEliminar"),
    path('categoria/detalles/<pk>/',v.CategoriaDetail,name="categoriaDetalle"),




    
]
