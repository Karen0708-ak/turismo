from django.urls import path
from . import views
urlpatterns=[
    path('inicioci',views.inicio,name='inicioci'),
]