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

def jugador(request):
    jugadores = Jugador.objects.all()
    return render(request, "equipo/jugadores.html", locals())

def entrenador(request):
    entrenadores = Entrenador.objects.all()
    return render(request, "equipo/entrenadores.html", locals())

def grafica(request):
    partidos = Partido.objects.all()
    #line = partidos.segundos(porcLine)
    return render(request, "grafica.html", locals())
    

    
    # Todos funciones de renderizar templates.:


def Line(request, id):
    partidos = Partido.objects.all()
    for partido in partidos:
        if partido.idPartido == id:
            line = partido.porcLine
            segundos = (line * 90)/50
    return render(request, "grafica.html", locals())

 