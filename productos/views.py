from django.shortcuts import render
from .models import Productos, CategoriaProds
# Create your views here.


def producto(request):
    productos = Productos.objects.all()
    return render(request, "productos/producto.html", {
        "productos": productos
    })