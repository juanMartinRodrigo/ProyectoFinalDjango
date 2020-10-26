from django.db import models

# Create your models here.

class Partido(models.Model):
    idPartido=models.CharField(max_length=8, default="", primary_key=True,)
    numLine=models.IntegerField()
    numScrum=models.IntegerField()
    numPenales=models.IntegerField()
    tri=models.IntegerField()
    numConversiones=models.IntegerField()
    numDrop=models.IntegerField()
    numTacles=models.IntegerField()
    numMaul=models.IntegerField()
    numRuck=models.IntegerField()
    cantPases=models.IntegerField()

class Error(models.Model):
    idError = models.CharField(max_length=8, primary_key=True,default="")
    numLinePerdidos=models.IntegerField()
    numScrumPerdidos=models.IntegerField()
    numPenalesEnContra=models.IntegerField()
    numPelotasCaidas=models.IntegerField()
    numConversionesErrados=models.IntegerField()
    numTaclesErrados=models.IntegerField()
    numPaseFoword=models.IntegerField()
    numDropErrados=models.IntegerField()
    numMaulErrados=models.IntegerField()
    numRuckErrados=models.IntegerField()

class Equipo(models.Model):
    club=models.CharField(max_length=35, default="Introduzca nombre del club", primary_key=True,)
    division=models.CharField(max_length=1, default="Introduzca division del club")
    cantJugadores=models.IntegerField()
    amonestados=models.IntegerField()
    expulsados=models.IntegerField()

class Jugador(models.Model):
    nombre=models.CharField(max_length=25, default="")
    apellido=models.CharField(max_length=25, default="")
    dni=models.IntegerField()
    tel=models.IntegerField()
    posicion=models.CharField(max_length=50, default="")
    asistenciaComp=models.BooleanField(default=False)
    gym=models.BooleanField(default=False)
    amonestado=models.BooleanField(default=False)
    expulsado=models.BooleanField(default=False)

class Entrenador(models.Model):
    nombre=models.CharField(max_length=25, default="")
    apellido=models.CharField(max_length=25, default="")
    dni=models.IntegerField()
    telefono=models.IntegerField()

class Estadistica(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    error = models.ForeignKey(Error, on_delete=models.CASCADE)
    