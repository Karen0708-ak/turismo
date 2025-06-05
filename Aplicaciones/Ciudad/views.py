from django.shortcuts import render,redirect
from .models import Ciudad
from .models import Lugares
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
    lugares_ids = request.POST.getlist("lugares")
    #Subiendo archivo
    foto=request.FILES.get("foto")
    #Archivo
    folleto=request.FILES.get("folleto")
    

    nuevaCiudad=Ciudad.objects.create(nombre=nombre,clima=clima,poblacion=poblacion,foto=foto,folleto=folleto)
    for id in lugares_ids:
            lugares = Lugares.objects.get(id=id)
            nuevaCiudad.lugares.add(lugares)
    #mensaje de confirmacion
    messages.success(request,"Ciudad guardada exitosamente")
    return redirect('inicioci')
def eliminarCiudad(request,id):
    ciudadEliminar=Ciudad.objects.get(id=id)
    ciudadEliminar.delete()
    #mensaje de confirmacion
    messages.success(request,"Ciudad ELIMINADO exitosamente")
    return redirect('inicioci')

def editarCiudad(request,id):
    ciudadEditar=Ciudad.objects.get(id=id)
    rlugares=Lugares.objects.all()
    lugares_actuales = ciudadEditar.lugares.values_list('id', flat=True)
    return render(request, "editarCiudad.html", {
        'ciudadEditar':ciudadEditar,
        'lugares': rlugares,
        'lugares_actuales': lugares_actuales
    })

def procesarEdicionCiudad(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    clima=request.POST["clima"]
    poblacion=request.POST["poblacion"]

    lugares_ids = request.POST.getlist("lugares")
    #Subiendo archivo
    nfoto=request.FILES.get("foto")
    #Archivo
    nfolleto=request.FILES.get("folleto")


    ciudad=Ciudad.objects.get(id=id)
    ciudad.nombre=nombre
    ciudad.clima=clima
    ciudad.poblacion=poblacion

    if nfoto:
        ciudad.foto= nfoto
    if nfolleto:
        ciudad.folleto= nfolleto
    ciudad.save()
    ciudad.lugares.clear()
    for id in lugares_ids:
            lugares = Lugares.objects.get(id_jugador=id)
            ciudad.lugares.add(lugares)

    #mensaje de confirmacion
    messages.success(request,"Ciudad ACTUALIZADA exitosamente")
    return redirect('inicioci')