from django import forms
from django.forms import ModelForm, Form
from core.models import *

            

class InputEquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
    
        fields = [
            'club',
            'division',
            'cantJugadores',
            'amonestados',
            'expulsados',
        ]
        labels = {
            'club': 'Club',
            'division': 'Division',
            'cantJugadores' : 'Cantidad De Jugadores',
            'amonestados': 'Cantidad De Amonestados',
            'expulsados': 'Cantidad De Expulsados',
        }
        widgets = {
            'club': forms.TextInput(attrs={'class':'form-control'}),
            'division': forms.TextInput(attrs={'class':'form-control'}),
            'cantJugadores': forms.NumberInput(attrs={'class':'form-control'}),
            'amonestados': forms.NumberInput(attrs={'class':'form-control'}),
            'expulsados' : forms.NumberInput(attrs={'class':'form-control'}),
        }

class InputJugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador

        fields = [
            'nombre',
            'apellido',
            'dni',
            'tel',
            'posicion',
            'asistenciaComp',
            'gym',
            'amonestado',
            'expulsado',
            'equipo',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni': 'DNI',
            'tel': 'Telefono',
            'posicion': 'Posicion',
            'asistenciaComp': 'Asistencia Completa',
            'gym': 'Va al gimnasio',
            'amonestado': 'Fue amonestado',
            'expulsado': 'Fue amonestado',
            'equipo': 'A que club va?',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.NumberInput(attrs={'class':'form-control'}),
            'tel': forms.NumberInput(attrs={'class':'form-control'}),
            'posicion': forms.TextInput(attrs={'class':'form-control'}),
            'asistenciaComp': forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'gym':  forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'amonestado':  forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'expulsado':  forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'equipo': forms.Select(attrs={'class':'form-control'}),
        }

class InputEntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador

        fields = [
            'nombre',
            'apellido',
            'dni',
            'telefono',
            'equipo',
        ]
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'dni': 'DNI',
            'telefono': 'Telefono',
            'equipo': 'A que Club Vas?'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.NumberInput(attrs={'class':'form-control'}),
            'telefono': forms.NumberInput(attrs={'class':'form-control'}),
            'equipo': forms.Select(attrs={'class':'form-control'}),
        }

class InputPartidoForm(forms.ModelForm):
    class Meta:
        model = Partido

        fields = [
            'idPartido',
            'equipo',
            'tri',
            'numLine' ,
            'numScrum',
            'numPenales',
            'numConversiones',
            'numDrop',
            'numTacles',
            'numMaul',
            'numRuck',
            'cantPases',
            'numLinePerdidos',
            'numScrumPerdidos',
            'numPenalesEnContra',
            'numPelotasCaidas',
            'numPaseFoword',
            'numConversionesErrados',
            'numDropErrados',
            'numTaclesErrados',
            'numMaulErrados',
            'numRuckErrados'
        ]
        labels = {
            'idPartido': 'IdPartido',
            'equipo': 'Que Equipo jugó',
            'tri': 'Try',
            'numLine': 'Line',
            'numScrum': 'Scrum',
            'numPenales': 'Penales',
            'numConversiones': 'Conversiones',
            'numDrop': 'Drops',
            'numTacles': 'Tacles',
            'numMaul': 'Mauls',
            'numRuck': 'Rucks',
            'cantPases': 'Pases',
            'numLinePerdidos': 'Line Perdidos',
            'numScrumPerdidos': 'Scrum Perdidos',
            'numPenalesEnContra': 'Penales En Contra',
            'numPelotasCaidas': 'Pelotas Caidas',
            'numPaseFoword': 'Pases Fowords',
            'numConversionesErrados': 'Conversiones Erradas',
            'numDropErrados': 'Drops Errados',
            'numTaclesErrados': 'Tacles Errados',
            'numMaulErrados': 'Mauls Perdidos',
            'numRuckErrados': 'Rucks Perdidos', 
        }
        widgets = {
            'idPartido': forms.NumberInput(attrs={'class':'form-control'}),
            'equipo': forms.Select(attrs={'class':'form-control'}),
            'tri': forms.NumberInput(attrs={'class':'form-control'}),
            'numLine': forms.NumberInput(attrs={'class':'form-control'}),
            'numScrum': forms.NumberInput(attrs={'class':'form-control'}),
            'numPenales': forms.NumberInput(attrs={'class':'form-control'}),
            'numConversiones': forms.NumberInput(attrs={'class':'form-control'}),
            'numDrop': forms.NumberInput(attrs={'class':'form-control'}),
            'numTacles': forms.NumberInput(attrs={'class':'form-control'}),
            'numMaul': forms.NumberInput(attrs={'class':'form-control'}),
            'numRuck': forms.NumberInput(attrs={'class':'form-control'}),
            'cantPases': forms.NumberInput(attrs={'class':'form-control'}),
            'numLinePerdidos': forms.NumberInput(attrs={'class':'form-control'}),
            'numScrumPerdidos': forms.NumberInput(attrs={'class':'form-control'}),
            'numPenalesEnContra': forms.NumberInput(attrs={'class':'form-control'}),
            'numPelotasCaidas': forms.NumberInput(attrs={'class':'form-control'}),
            'numPaseFoword': forms.NumberInput(attrs={'class':'form-control'}),
            'numConversionesErrados': forms.NumberInput(attrs={'class':'form-control'}),
            'numDropErrados': forms.NumberInput(attrs={'class':'form-control'}),
            'numTaclesErrados': forms.NumberInput(attrs={'class':'form-control'}),
            'numMaulErrados': forms.NumberInput(attrs={'class':'form-control'}),
            'numRuckErrados': forms.NumberInput(attrs={'class':'form-control'}),
        }
    