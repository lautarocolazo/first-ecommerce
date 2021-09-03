from django.shortcuts import render, redirect
from .forms import FormularioContacto
# Create your views here.

def contacto(request):
    form_contacto = FormularioContacto()

    if request.method == "POST":
        form_contacto = FormularioContacto(data=request.POST)
        if form_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            return redirect("/contacto/?valido")

    return render(request,"contacto/contacto.html",{
        "form_contacto": form_contacto
    })