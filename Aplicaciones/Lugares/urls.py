from django.urls import path
from . import views
urlpatterns=[
    path('iniciolu',views.inicio,name='iniciolu'),
    path('nuevoLugar',views.nuevoLugar),
    path('guardarLugar',views.guardarLugar),
    path('eliminarLugar/<id>',views.eliminarLugar),
    path('procesarEdicionLugar',views.procesarEdicionLugar),
    path('editarLugar/<id>',views.editarLugar),
]