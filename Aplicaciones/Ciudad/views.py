from django.shortcuts import render
from .models import Ciudad
# Create your views here.
def inicio(request):
    listadoCiudad=Ciudad.objects.all()
    return render(request,"inicioci.html",{'ciudad':listadoCiudad})