from django.urls import path
from . import views
urlpatterns=[
    path('inicioci',views.inicio,name='inicioci'),
    path('nuevaCiudad',views.nuevaCiudad),
    path('guardarCiudad',views.guardarCiudad),
    path('eliminarCiudad/<id>',views.eliminarCiudad),
    path('procesarEdicionCiudad',views.procesarEdicionCiudad),
    path('editarCiudad/<id>',views.editarCiudad),
]
