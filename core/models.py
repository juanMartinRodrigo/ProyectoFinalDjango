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

    def segundos (self):
        porcentaje = 0
        segundos = (porcentaje * 90)/50
        return segundosf

class Equipo(models.Model):
    club=models.CharField(max_length=35, primary_key=True,)
    division=models.CharField(max_length=1, )
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
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE);

class Entrenador(models.Model):
    nombre=models.CharField(max_length=25, default="")
    apellido=models.CharField(max_length=25, default="")
    dni=models.IntegerField()
    telefono=models.IntegerField()
    #equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE);
    
    