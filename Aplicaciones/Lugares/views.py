from django.shortcuts import render,redirect

from .models import Lugares
from django.contrib import messages

# Create your views here.

def inicio(request):
    listadoLugares=Lugares.objects.all()
    return render(request,"iniciolu.html",{'lugar':listadoLugares})
def nuevoLugar(request):
    return render(request,"nuevosLugares.html")
def guardarLugar(request):
    nombre=request.POST["nombre"]
    direccion=request.POST["direccion"]
    resena=request.POST["resena"]
    horario=request.FILES.get("horario")
    historia=request.FILES.get("historia")
    

    nuevoLugar=Lugares.objects.create(nombre=nombre,direccion=direccion,resena=resena,horario=horario,historia=historia)
    #mensaje de confirmacion
    messages.success(request,"Lugar guardada exitosamente")
    return redirect('iniciolu')
def eliminarLugar(request,id):
    lugarEliminar=Lugares.objects.get(id=id)
    lugarEliminar.delete()
    #mensaje de confirmacion
    messages.success(request,"Lugar ELIMINADO exitosamente")
    return redirect('iniciolu')

def editarLugar(request,id):
    lugarEditar=Lugares.objects.get(id=id)
    return render(request,"editarLugares.html",{'lugarEditar':lugarEditar})

def procesarEdicionCiudad(request):
    nombre=request.POST["nombre"]
    direccion=request.POST["direccion"]
    resena=request.POST["resena"]
    horario=request.FILES.get("horario")
    historia=request.FILES.get("historia")
    #Subiendo archivo
    nhorario=request.FILES.get("horario")
    #Archivo
    nhistoria=request.FILES.get("historia")


    lugar=Lugares.objects.get(id=id)
    lugar.nombre=nombre
    lugar.direccion=direccion
    lugar.resena=resena

    if nhorario:
        lugar.horario= nhorario
    if nhistoria:
        lugar.historia= nhistoria
    lugar.save()

    #mensaje de confirmacion
    messages.success(request,"Lugar ACTUALIZADo exitosamente")
    return redirect('iniciolu')