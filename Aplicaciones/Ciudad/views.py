from django.shortcuts import render,redirect
from .models import Ciudad
# Create your views here.
from django.contrib import messages

def inicio(request):
    listadoCiudad=Ciudad.objects.all()
    return render(request,"inicioci.html",{'ciudad':listadoCiudad})
def nuevaCiudad(request):
    return render(request,"nuevaCiudad.html")
#Almacenando los datos de cargo en la Bdd
def guardarCiudad(request):
    nombre=request.POST["nombre"]
    clima=request.POST["clima"]
    poblacion=request.POST["poblacion"]

    #Subiendo archivo
    foto=request.FILES.get("foto")
    #Archivo
    folleto=request.FILES.get("folleto")

    nuevaCiudad=Ciudad.objects.create(nombre=nombre,clima=clima,poblacion=poblacion,foto=foto,folleto=folleto)
    #mensaje de confirmacion
    messages.success(request,"Ciudad guardada exitosamente")
    return redirect('inicioci')