from django.contrib import admin
from core.models import *

class EquipoAdmin(admin.ModelAdmin):
    search_fields =['club']
    list_display = ['club','division','cantJugadores','amonestados','expulsados',]
    fieldsets = (
            ('Nombre de club',  {'fields': ('club',)}),
            ('Datos sobre el equipo',  {'fields': ('division','cantJugadores','amonestados','expulsados',)}),
    )   
    
class JugadorAdmin(admin.ModelAdmin):
    search_fields = ['nombre','apellido','dni']
    fieldsets = (
            ('Datos de Personal', {'fields': ('nombre', 'apellido', 'dni',)}),
            ('Contacto ', {'fields': ('tel',)}),
            ('Datos del Jugador', {'fields': ('equipo','posicion','gym','asistenciaComp','amonestado','expulsado',)}),
    )
    list_display = ['nombre', 'apellido', 'dni','tel','equipo','posicion','gym','asistenciaComp','amonestado','expulsado',]
    
class EntrenadorAdmin(admin.ModelAdmin):
	list_display = ['nombre', 'apellido', 'dni','telefono','equipo', ]
	fieldsets = (
            ('Datos de Personal', {'fields': ('nombre', 'apellido', 'dni',)}),
            ('Club ', {'fields': ('equipo',)}),
            ('Contacto ', {'fields': ('telefono',)}),
    )
	search_fields = ['nombre','apellido','dni']

class PartidoAdmin(admin.ModelAdmin):
    search_fields = ['idPartido']
    fieldsets = (
            ('ID', {'fields': ('idPartido',)}),
            ('Cantidad de try', {'fields': ('tri',)}),
            ('Datos de Partido', {'fields': ('numLine','numScrum','numPenales','numConversiones','numDrop','numTacles','numMaul','numRuck','cantPases',)}),
            ('Errores de los Fowers', {'fields': ('numLinePerdidos','numScrumPerdidos','numMaulErrados','numRuckErrados',)}),
            ('Errores de los 3/4', {'fields': ('numConversionesErrados','numDropErrados',)}),
            ('Errores de el Equipo', {'fields': ('numPenalesEnContra','numPelotasCaidas','numPaseFoword','numTaclesErrados',)}),
    )
    list_display = ['tri', 'idPartido','numLine','numScrum','numPenales','numConversiones','numDrop','numTacles','numMaul','numRuck','cantPases','numPenalesEnContra','numPelotasCaidas','numPaseFoword','numTaclesErrados','numConversionesErrados','numDropErrados','numLinePerdidos','numScrumPerdidos','numMaulErrados','numRuckErrados',]


# Register your models here.
admin.site.register(Jugador,JugadorAdmin);
admin.site.register(Equipo,EquipoAdmin);
admin.site.register(Partido,PartidoAdmin);
admin.site.register(Entrenador, EntrenadorAdmin);
