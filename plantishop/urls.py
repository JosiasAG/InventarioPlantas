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
from django.contrib.auth import views as views_auth

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
    path('buscar_compra/', views.buscarCompra, name='buscar_compra'),
    path('buscar_venta/', views.buscarVenta, name='buscar_venta'),
    path('consultar_compra/<int:Nconsulta>', views.consultarCompra, name='consultar_compra'),
    path('consultar_venta/<int:Nconsulta>', views.consultarVenta, name='consultar_venta'),
    path('editar_compra/<int:Nconsulta>', views.editarCompra, name='editar_compra'),
    path('editar_venta/<int:Nconsulta>', views.editarVenta, name='editar_venta'),
    path('eliminar_compra/<int:Nconsulta>', views.eliminarCompra, name='eliminar_compra'),
    path('eliminar_venta/<int:Nconsulta>', views.eliminarVenta, name='eliminar_venta'),
    path('hacer_inventario/', views.hacerInventario, name='hacer_inventario'),
    path('recuperar_contrasena/', views_auth.PasswordResetView.as_view(template_name = 'recuperar_contrasenaH.html'), name='password_reset'),
    path('enviar_email/', views_auth.PasswordResetDoneView.as_view(template_name = 'revisar_correoH.html'), name='password_reset_done'),
    path('confirmar_email/<uidb64>/<token>', views_auth.PasswordResetConfirmView.as_view(template_name = 'cambiar_contrasenaH.html'), name='password_reset_confirm'),
    path('cambiar_contraseña/', views_auth.PasswordResetCompleteView.as_view(template_name= 'correo_recuperadoH.html'), name='password_reset_complete'),
    
]
