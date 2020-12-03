from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, ListView
from core.models import *
from core.forms import *


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

def equipo(request):
    equipos = Equipo.objects.all()
    return render(request, "equipo.html", locals())

def inputEquipo(request):
    if request.method == 'POST':
        form = InputEquipoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('equipo')
    else:
        form = InputEquipoForm()
    
    return render(request, "equipo/inputEquipo.html", {'form': form})

def partido(request):
    partidos = Partido.objects.all()
    return render(request, "partidos.html", locals())

def inputPartido(request):
    if request.method == 'POST':
        form = InputPartidoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('partidos')
    else:
        form = InputPartidoForm()

    return render(request, "partido/inputPartido.html", {'form': form})

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
    return render(request, "equipo/inputJugador.html", {'form': form})

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
    return render(request, "equipo/inputEntrenador.html", {'form': form})

def grafaaica(request):
    partidos = Partido.objects.all()
    return render(request, "partido/grafica.html",locals())

class grafica(TemplateView):
    model = Partido
    template_name = 'partido/grafica.html'

    def post(self, request, *args, **kwargs):
        data= {}
        try:
            action = request.POST['action']
            if action == 'select_option':
                pass
            else:
                data['error'] = 'Ha ocurrido un ERROR'
        except exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        
    def get_context_data(self, **kwargs):
        context = super(grafica, self).get_context_data(**kwargs)
        context['form'] = graficaSelect()
        return context

    #return render(request, "partido/grafica.html", {'form': form})
    # Todos funciones de renderizar templates.:


 