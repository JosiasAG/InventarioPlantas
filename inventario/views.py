from django.shortcuts import render, redirect
from .forms import inventarioForms, incomingForm, outcomingForm, userForm
from .models import productsModel, incomingProducts, outcomingProducts
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Max
from django.contrib.auth import views as views_auth


def inicio(request):
    return render(request, 'inicioH.html')


def registrar(request):
    if request.method == 'GET':
        return render(request, 'registroH.html', {'registro': userForm})
    else:
        if len(request.POST['username'])>0 and len(request.POST['password1'])>0:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(
                        username = request.POST['username'],
                        first_name = request.POST['first_name'],
                        last_name = request.POST['last_name'],
                        email = request.POST['email'],
                        password = request.POST['password1'],
                    )
                    user.save()
                    return redirect('ingreso')
                except IntegrityError:
                    return render(request, 'registroH.html', {'registro': userForm, 'error': 'El usuario ya existe'})
            else:
                return render(request, 'registroH.html', {'registro': userForm, 'error': 'Las contraseñas no coinciden'})
        else:
            return render(request, 'registroH.html', {'registro': userForm})


def ingresar(request):
    if request.method == 'GET':
        return render(request, 'ingresarH.html', {'ingresar': AuthenticationForm})
    else:
        user = authenticate(
            request, username = request.POST['username'], password = request.POST
            ['password'])
        print(request.POST)
        if user is None:
            return render(request, 'ingresarH.html', {'ingresar': AuthenticationForm, 'error': 'Usuario y/o contraseña incorrectos'})
        else:
            login(request, user)
            return redirect('inicio') 
        

def salir(request):
    logout(request)
    return redirect('inicio')

@login_required
def inventarioP(request):
    if request.method == 'GET':
        return render(request, 'inventario.html', {'inventario': inventarioForms})
    else:
        producto = productsModel.objects.create(
            product = request.POST['product'],
            description = request.POST['description'],
            category = request.POST['category'],
            initial_stock = int(request.POST['initial_stock'])
        )
        producto.save()
        return render(request, 'inventario.html', {'inventario': inventarioForms})


    
@login_required
def busqueda(request):
    if request.method == 'GET':
        return render(request, 'busquedaH.html')
    else:
        find = productsModel.objects.all().filter(product__icontains=request.POST['product'])
        return render(request, 'busquedaH.html',{'resultado': find})

@login_required
def consultar(request, Nconsulta):
    if request.method == 'GET': 
        obtain = get_object_or_404(productsModel, id = Nconsulta)
        return render(request, 'consultaH.html', {'consulta': obtain})
    else:
        return redirect('editar_producto')

@login_required
def editarProducto(request, Nconsulta):
    obtain = get_object_or_404(productsModel, id = Nconsulta)
    edit = inventarioForms(instance=obtain)
    
    if request.method == 'POST':
        form = inventarioForms(request.POST, instance=obtain)
        if form.is_valid():
            form.save()
            return redirect('consultar', Nconsulta=Nconsulta)
        return render(request, 'editarH.html', {'edicion': edit, 'clave': Nconsulta})
    else:
        form = inventarioForms(instance=obtain)
    return render(request, 'editarH.html', {'edicion': edit, 'clave': Nconsulta}) 
        


@login_required
def agregarProducto(request):
    if request.method == 'GET':
        return render(request,'agregarH.html', {'agregar': incomingForm})
    else:
        agregar = productsModel.objects.get(id = request.POST['code'])
        guardar = incomingProducts.objects.create(
            code = agregar,
            supplier = request.POST['supplier'],
            name = request.POST['name'],
            address = request.POST['address'],
            telephone = request.POST['telephone'],
            email = request.POST['email'],
            bill = request.POST['bill'],
            quantityIncoming = request.POST['quantityIncoming'],
            unit_price = request.POST['unit_price'],
        )
        agregar.save()
        guardar.save()
        return render(request,'agregarH.html', {'agregar': incomingForm})


@login_required    
def eliminarProducto(request, Nconsulta):
    if request.method == 'POST':
        obtain = get_object_or_404(productsModel, id = Nconsulta)
        obtain.delete()
        return redirect('buscar')
    return redirect('buscar')


@login_required
def buscarCompra(request):
    if request.method == 'GET':
        return render(request, 'buscarCompraH.html')
    else:
        find = incomingProducts.objects.all().filter(bill__icontains=request.POST['bill'])
        return render(request, 'buscarCompraH.html',{'resultado': find})


@login_required
def consultarCompra(request, Nconsulta):
    if request.method == 'GET': 
        obtain = get_object_or_404(incomingProducts, id = Nconsulta)
        return render(request, 'consultaCompraH.html', {'consulta': obtain})
    else:
        return redirect('editar_producto')

@login_required
def editarCompra(request, Nconsulta):
    obtain = get_object_or_404(incomingProducts, id = Nconsulta)
    edit = incomingForm(instance=obtain)
    
    if request.method == 'POST':
        form = incomingForm(request.POST, instance=obtain)
        if form.is_valid():
            form.save()
            return redirect('consultar_compra', Nconsulta=Nconsulta)
        return render(request, 'editarCompraH.html', {'edicion': edit, 'clave': Nconsulta})
    else:
        form = incomingForm(instance=obtain)
    return render(request, 'editarCompraH.html', {'edicion': edit, 'clave': Nconsulta}) 


@login_required    
def eliminarCompra(request, Nconsulta):
    if request.method == 'POST':
        obtain = get_object_or_404(incomingProducts, id = Nconsulta)
        obtain.delete()
        return redirect('buscar_compra')
    return redirect('buscar_compra')
        
    
@login_required
def venderProducto(request):
    if request.method == 'GET':
        return render(request,'eliminarH.html', {'eliminar': outcomingForm})
    else:
        agregar = productsModel.objects.get(id = request.POST['code'])
        verificar = outcomingProducts.objects.aggregate(verificar = Max('bill'))
        if verificar is not None: 
            verificar = int(verificar['verificar']) + 1
            joint = str(verificar).zfill(8)
        else:
            verificar = int(verificar['verificar']) + 1
            joint = str(verificar).zfill(8)
        if agregar.summatory >= int(request.POST['quantityOutcoming']):
            guardar = outcomingProducts.objects.create(
                code = agregar,
                bill = joint,
                quantityOutcoming = request.POST['quantityOutcoming'],
                unit_price = int(request.POST['quantityOutcoming']) * int(agregar.price)
        )
            agregar.save()
            guardar.save()
            return render(request,'eliminarH.html', {'eliminar': outcomingForm})
        else:
            return render(request,'eliminarH.html', {'eliminar': outcomingForm, 'error': f'Stock insuficiente para venta, existen {agregar.summatory} pieza(s)'})
        
        
@login_required
def buscarVenta(request):
    if request.method == 'GET':
        return render(request, 'buscarVentaH.html')
    else:
        find = outcomingProducts.objects.all().filter(bill__icontains=request.POST['bill'])
        return render(request, 'buscarVentaH.html',{'resultado': find})
    
    
@login_required
def consultarVenta(request, Nconsulta):
    if request.method == 'GET': 
        obtain = get_object_or_404(outcomingProducts, id = Nconsulta)
        return render(request, 'consultaVentaH.html', {'consulta': obtain})
    else:
        return redirect('editar_producto')


@login_required
def editarVenta(request, Nconsulta):
    obtain = get_object_or_404(outcomingProducts, id = Nconsulta)
    edit = outcomingForm(instance=obtain)
    
    if request.method == 'POST':
        form = outcomingForm(request.POST, instance=obtain)
        if form.is_valid():
            form.save()
            return redirect('consultar_venta', Nconsulta=Nconsulta)
        return render(request, 'editarVentaH.html', {'edicion': edit, 'clave': Nconsulta})
    else:
        form = outcomingForm(instance=obtain)
    return render(request, 'editarVentaH.html', {'edicion': edit, 'clave': Nconsulta}) 


@login_required    
def eliminarVenta(request, Nconsulta):
    if request.method == 'POST':
        obtain = get_object_or_404(outcomingProducts, id = Nconsulta)
        obtain.delete()
        return redirect('buscar_venta')
    return redirect('buscar_venta')

@login_required    
def hacerInventario(request):
    obtain = productsModel.objects.all()
    return render(request, 'hacerInventarioH.html', {'lista': obtain})