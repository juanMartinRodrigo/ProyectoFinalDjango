from django.urls import path,include
from django.contrib.auth.views import LoginView
from core.views import *
from . import views

urlpatterns = [
    path('core/login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('accounts/logout',logoutView,name="logout_url"),
    path('', HomeView.as_view(), name='home'),
    path('equipo', views.equipo, name="equipo"),
    path('inputEquipo', views.inputEquipo, name="inputEquipo"),
    path('partidos', views.partido, name="partidos"),
    path('inputPartido', views.inputPartido, name="inputPartido"),
    path('entrenadores', views.entrenador, name="entrenadores"),
    path('inputEntrenador', views.inputEntrenador, name="inputEntrenador"),
    path('jugadores', views.jugador, name="jugadores"),
    path('inputJugador', views.inputJugador, name="inputJugador"),
    path('test', views.test, name="test"), 
    path('grafica', grafica.as_view(), name="grafica"),
   
]