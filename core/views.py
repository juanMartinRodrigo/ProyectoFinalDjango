from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import *


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

def equipo(request):
    equipos = Equipo.objects.all()
    return render(request, "equipo.html", locals())

def partido(request):
    partidos = Partido.objects.all()
    return render(request, "partidos.html", locals())

def inputPartido(request):
    return render(request, "partido/inputPartido.html", )

def jugador(request):
    jugadores = Jugador.objects.all()
    return render(request, "equipo/jugadores.html", locals())

def entrenador(request):
    entrenadores = Entrenador.objects.all()
    return render(request, "equipo/entrenadores.html", locals())

def grafica(request):
    partidos = Partido.objects.all()
    #line = partidos.segundos(porcLine)
    return render(request, "partido/grafica.html", locals())
    

    
    # Todos funciones de renderizar templates.:


 