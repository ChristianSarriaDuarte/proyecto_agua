from django.shortcuts import render, redirect
from .models import Pedido
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
import random
import string
# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    pedidosListados = Pedido.objects.all()
    return render(request, "gestionPedidos.html", {"pedidos": pedidosListados})

def registrarPedido(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']

    pedido = Pedido.objects.create(codigo=codigo, nombre=nombre, cantidad=cantidad)
    return redirect('home')

def edicionPedido(request, codigo):
    pedido = Pedido.objects.get(codigo=codigo)
    return render(request, "edicionPedido.html", {"pedido": pedido})

def editarPedido(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    cantidad = request.POST['numCantidad']

    pedido = Pedido.objects.get(codigo=codigo)
    pedido.nombre = nombre
    pedido.cantidad = cantidad
    pedido.save()

    return redirect('home')


def eliminarPedido(request, codigo):
    pedido = Pedido.objects.get(codigo=codigo)
    pedido.delete()
    return redirect('home')
    

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('index')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las Contraseñas no coinciden'
                })

def signout(request):
    logout(request)
    return redirect('index')

def venta_de_agua(request):
    return render(request, 'venta_de_agua.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def confirmar_compra(request):
    if request.method == 'POST':
        # Obtener los datos del carrito
        orders_data = request.POST.get('orders')
        orders = eval(orders_data)  # Evaluar la cadena JSON

        for order in orders:
            # Generar un código de pedido único
            codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

            # Verificar que el código no exista ya
            while Pedido.objects.filter(codigo=codigo).exists():
                codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

            # Crear un nuevo pedido
            Pedido.objects.create(
                codigo=codigo,
                nombre=order['name'],
                cantidad=order['quantity']
            )
        
        # Limpiar el carrito después de la compra
        orders.clear()

        return redirect('catalogo')

    return redirect('catalogo')