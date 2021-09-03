from django.shortcuts import render,redirect
from productos.models import *
from .carro import Carro
# Create your views here.


def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return render(request, "carro/carro.html")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return render(request, "carro/carro.html")

def restar_producto(request, producto_id):
    carro=Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return render(request, "carro/carro.html")

def limpiar_carro(request):
    carro=Carro(request)
    carro.limpiar_carro()
    return render(request, "carro/carro.html")



def carro(request):
    return render(request, "carro/carro.html")