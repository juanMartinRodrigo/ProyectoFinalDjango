from django.urls import path,include
from core.views import *
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('equipo', views.equipo, name="equipo"),
    path('inputEquipo', views.inputEquipo, name="inputEquipo"),
    path('partidos', views.partido, name="partidos"),
    path('inputPartido', views.inputPartido, name="inputPartido"),
    path('entrenadores', views.entrenador, name="entrenadores"),
    path('inputEntrenador', views.inputEntrenador, name="inputEntrenador"),
    path('jugadores', views.jugador, name="jugadores"),
    path('inputJugador', views.inputJugador, name="inputJugador"),
    path('grafica', grafica.as_view(), name="grafica"),

    

    
]