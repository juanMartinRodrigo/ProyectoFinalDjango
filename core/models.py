from django.db import models

# Create your models here.

class Partido(models.Model):
    idPartido=models.CharField(max_length=8, default="", primary_key=True,)
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
    numLine=models.IntegerField(null = True)
    numScrum=models.IntegerField(null = True)
    numPenales=models.IntegerField(null = True)
    tri=models.IntegerField(null = True)
    numConversiones=models.IntegerField(null = True)
    numDrop=models.IntegerField(null = True)
    numTacles=models.IntegerField(null = True)
    numMaul=models.IntegerField(null = True)
    numRuck=models.IntegerField(null = True)
    cantPases=models.IntegerField(null = True)
    numLinePerdidos=models.IntegerField(null = True)
    numScrumPerdidos=models.IntegerField(null = True)
    numPenalesEnContra=models.IntegerField(null = True)
    numPelotasCaidas=models.IntegerField(null = True)
    numConversionesErrados=models.IntegerField(null = True)
    numTaclesErrados=models.IntegerField(null = True)
    numPaseFoword=models.IntegerField(null = True)
    numDropErrados=models.IntegerField(null = True)
    numMaulErrados=models.IntegerField(null = True)
    numRuckErrados=models.IntegerField(null = True)

    def porcLine (self):
        v = self.numLinePerdidos / self.numLine
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcScrum (self):
        v = self.numScrumPerdidos / self.numScrum
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcPenales (self):
        v = self.numPenalesEnContra / self.numPenales
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcConver (self):
        v = self.numConversionesErrados / self.numConversiones
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcDrop (self):
        v = self.numDropErrados / self.numDrop
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcTacles (self):
        v = self.numTaclesErrados / self.numTacles
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcPases (self):
        p = self.numPaseFoword + self.numPelotasCaidas
        v = p / self.cantPases
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcRuck(self):
        v = self.numRuckErrados / self.numRuck
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcMaules(self):
        v = self.numMaulErrados / self.numMaul
        porc = int(v*100)
        porc = 100 - porc
        return porc

class Equipo(models.Model):
    club=models.CharField(max_length=35, primary_key=True,)
    division=models.CharField(max_length=1, )
    cantJugadores=models.IntegerField(null = True)
    amonestados=models.IntegerField(null = True)
    expulsados=models.IntegerField(null = True)

class Jugador(models.Model):
    nombre=models.CharField(max_length=25, default="")
    apellido=models.CharField(max_length=25, default="")
    dni=models.IntegerField(null = True)
    tel=models.IntegerField(null = True)
    posicion=models.CharField(max_length=50, default="")
    asistenciaComp=models.BooleanField(default=False)
    gym=models.BooleanField(default=False)
    amonestado=models.BooleanField(default=False)
    expulsado=models.BooleanField(default=False)
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)

class Entrenador(models.Model):
    nombre=models.CharField(max_length=25, default="")
    apellido=models.CharField(max_length=25, default="")
    dni=models.IntegerField(null = True)
    telefono=models.IntegerField(null = True)
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)
    
    