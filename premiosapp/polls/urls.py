from django.urls import path

from . import views #El . es para indicar que es del mismo paquete polls

urlpatterns = [
    path('', views.index, name='index')
]