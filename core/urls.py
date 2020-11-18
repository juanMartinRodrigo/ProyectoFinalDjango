from django.urls import path,include
from .views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('equipo', views.equipo, name="equipo"),
    path('partidos', views.partido, name="partidos"),
    path('entrenadores', views.entrenador, name="entrenadores"),
    path('jugadores', views.jugador, name="jugadores"),
    path('grafica', views.grafica, name="grafica")

    
]