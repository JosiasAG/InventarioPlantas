"""
URL configuration for plantishop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('inventario/',views.inventarioP, name='inventario'),
    path('registro/', views.registrar, name='registrar'),
    path('ingreso/', views.ingresar, name='ingreso'),
    path('salir/', views.salir, name='salir'),
    path('buscar/', views.busqueda, name='buscar'),
    path('consultar/<int:Nconsulta>', views.consultar, name='consultar'),
    path('editar_producto/<int:Nconsulta>',  views.editarProducto, name='editar_producto'),
    path('agregar_producto/', views.agregarProducto, name='agregar_producto'),
    path('vender_producto/', views.venderProducto, name='vender_producto'),
    path('eliminar/<int:Nconsulta>', views.eliminarProducto, name='eliminar'),
    #path('buscar_compra/', views.buscarVenta, name='buscar_compra'),
    path('buscar_venta/', views.buscarVenta, name='buscar_venta'),
    path('consultar_venta/<int:Nconsulta>', views.consultarVenta, name='consultar_venta'),
    path('editar_venta/<int:Nconsulta>', views.editarVenta, name='editar_venta'),
    
]
