from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, ListView
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from core.models import *
from core.forms import *


# Create your views here.

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_url")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login_url")


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['estadisticas'] = Estadistica.objects.all()
        return context
    
def equipo(request):
    equipos = Equipo.objects.all().order_by('club')
    return render(request, "equipo.html", locals())

def inputEquipo(request):
    if request.method == 'POST':
        form = InputEquipoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('equipo')
    else:
        form = InputEquipoForm()
    
    return render(request, "input/inputEquipo.html", {'form': form})

def partido(request):
    partidos = Partido.objects.all()
    errores = Error.objects.all()
    return render(request, "partidos.html", locals())

def inputPartido(request):
    if request.method == 'POST':
        form = InputPartidoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('partidos')
    else:
        form = InputPartidoForm()

    return render(request, "input/inputPartido.html", {'form': form})

def jugador(request):
    jugadores = Jugador.objects.all()
    return render(request, "equipo/jugadores.html", locals())

def inputJugador(request):
    if request.method == 'POST':
        form = InputJugadorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('jugadores')
    else:
        form = InputJugadorForm()
    return render(request, "input/inputJugador.html", {'form': form})

def entrenador(request):
    entrenadores = Entrenador.objects.all()
    return render(request, "equipo/entrenadores.html", locals())

def inputEntrenador(request):
    if request.method == 'POST':
        form = InputEntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('entrenadores')
    else:
        form = InputEntrenadorForm()
    return render(request, "input/inputEntrenador.html", {'form': form})

def inputError(request):
    if request.method == 'POST':
        form = InputErroresForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('partidos')
    else:
        form = InputErroresForm()

    return render(request, "input/inputError.html", {'form': form})

def inputEstadistica(request):
    if request.method == 'POST':
        form = InputEstadisticaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = InputEstadisticaForm()
    return render(request, "input/inputEstadistica.html", {'form': form})

class grafica(TemplateView):
    template_name = 'partido/grafica.html'
        
    def get_context_data(self, **kwargs):
        context = super(grafica, self).get_context_data(**kwargs)
        context['form'] = graficaSelect()
        context['partidos'] = Partido.objects.all()
        context['variable'] = "hola"
        return context
    

@csrf_protect
def test(request):
    if request.method == 'POST':
        partidos = Partido.objects.all()
        data = serializers.serialize("json", partidos)
        return HttpResponse(data, content_type='application/json')


 