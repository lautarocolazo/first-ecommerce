from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.views.generic import CreateView
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from productos.models import Productos, CategoriaProds
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from carro.carro import *
from carro.views import *


# Create your views here.

#Index view
@login_required(login_url="login")
def index(request):
    productos = Productos.objects.all()
    categorias = CategoriaProds.objects.all()
    return render(request, "proyectofinal/index.html",{
        "productos": productos,
        "categorias": categorias,
    })

#About view
def about(request):
    return render(request, "proyectofinal/about.html")
    

#Login View
def login_view(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Username OR password is incorrect")
        
    return render(request, "proyectofinal/login.html",{

    })

#Logout function
def logoutUser(request):
    logout(request)
    return redirect('login')

#Register function
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'proyectofinal/register.html'
    success_url = reverse_lazy('login')
# def register(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#     else:
#         form = CreateUserForm()

#         if request.method == "POST":
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get("username")
#                 messages.success(request, f"La cuenta fue creada para {user}")
#                 return redirect('login')

#     return render(request, "proyectofinal/register.html", {
#         "form": form
#     })

#Search View
@login_required(login_url="login")
def search(request):
    productos = Productos.objects.all()
    queryset = request.GET.get('search')
    if queryset:
        lista = 1
        resultados = Productos.objects.filter(
      Q(titulo__icontains=queryset) | Q(contenido__icontains=queryset)
    ).distinct()
        return render(request, "proyectofinal/search.html",{
            "resultados": resultados,
            "queryset": queryset
        })
    else:
        return render(request, "proyectofinal/search.html",{
            "productos": productos
        })
    # productos = Productos.objects.all()

    # if request.method == "POST":
    #     search = request.POST['search']
    #     resultados = Productos.objects.filter(contenido__icontains=search)

    #     return render(request, "proyectofinal/search.html",{
    #         "productos": productos,
    #         "search": search,
    #         "resultados": resultados
    #     })
    # else:
    #     return render(request, "proyectofinal/search.html",{
    #         "productos": productos
    #     })

#Product view
@login_required(login_url="login")
def producto_detalle(request, id):
    producto = Productos.objects.all().get(pk=id)
    return render(request, "proyectofinal/producto_detalle.html", {
        'producto': producto,
    })


# @login_required(login_url="login")
# def categories(request, categoriaProd_id):
#     productos = Productos.objects.filter(categorias=categoriaProd_id)
#     categories = CategoriaProds.objects.get(id=categoriaProd_id)
#     return render(request, "proyectofinal/search_categorias.html", {
#         'productos': productos,
#         'categorias': categories,
#     })

