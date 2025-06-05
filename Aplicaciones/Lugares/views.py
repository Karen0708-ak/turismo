from django.shortcuts import render

from .models import Lugares
from django.contrib import messages

# Create your views here.

def inicio(request):
    listadoLugares=Lugares.objects.all()
    return render(request,"iniciolu.html",{'lugar':listadoLugares})