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
            ('Fecha y Lugar', {'fields': ('fecha','lugar',)}),
            ('Tu equipos al Jugar', {'fields': ('equipo_1',)}),
            ('VS',{'fields': ('equipo_2',)}),
            ('Cantidad de try', {'fields': ('tri',)}),
            ('Datos de Partido', {'fields': ('numLine','numScrum','numPenales','numConversiones','numDrop','numTacles','numMaul','numRuck','cantPases',)}),
    )
    list_display = ['tri', 'fecha','lugar','equipo_1','equipo_2','numLine','numScrum','numPenales','numConversiones','numDrop','numTacles','numMaul','numRuck','cantPases',]

class ErrorAdmin(admin.ModelAdmin):
    list_display = ['numLinePerdidos','numScrumPerdidos','numMaulErrados','numRuckErrados','numConversionesErrados','numDropErrados','numPenalesEnContra','numPelotasCaidas','numPaseFoword','numTaclesErrados',]
    fieldsets = (
        ('Errores de los Fowers', {'fields': ('numLinePerdidos','numScrumPerdidos','numMaulErrados','numRuckErrados',)}),
        ('Errores de los 3/4', {'fields': ('numConversionesErrados','numDropErrados',)}),
        ('Errores de el Equipo', {'fields': ('numPenalesEnContra','numPelotasCaidas','numPaseFoword','numTaclesErrados',)}),
)

class EstadisticaAdmin(admin.ModelAdmin):
    list_display = ['partido', 'error']
    fieldsets = (
        ('informacion', {'fields': ('partido', 'error',)}),
    )

# Register your models here.
admin.site.register(Equipo,EquipoAdmin);
admin.site.register(Jugador,JugadorAdmin);
admin.site.register(Entrenador, EntrenadorAdmin);
admin.site.register(Partido,PartidoAdmin);
admin.site.register(Error,ErrorAdmin);
admin.site.register(Estadistica,EstadisticaAdmin);
