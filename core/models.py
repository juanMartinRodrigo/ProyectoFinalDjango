from django.db import models

# Create your models here.

posiciones = [
    ('0', 'DESCONOCIDO'),
    ('1', 'Pilar Izquierdo'),
    ('2','Hooker'),
    ('3','Pilar Derecho'),
    ('4','Segunda Linea Izquierdo'),
    ('5','Segunda Linea Derecho'),
    ('6','Ala Derecho'),
    ('7','Ala Izquierdp'),
    ('8','8'),
    ('9','Medio Scrum'),
    ('10','Apertura'),
    ('11','Wing Izquierdo'),
    ('12','Primer Centro'),
    ('13','Segundo Centro'),
    ('14','Wing Derecho'),
    ('15','Full Back'),
]

class Equipo(models.Model):
    club=models.CharField(max_length=35, primary_key=True)
    division=models.CharField(max_length=1, )
    cantJugadores=models.IntegerField(null = False)
    amonestados=models.IntegerField(null = False)
    expulsados=models.IntegerField(null = False)

class Jugador(models.Model):
    nombre=models.CharField(max_length=25, default="")
    apellido=models.CharField(max_length=25, default="")
    dni=models.IntegerField(null = False)
    tel=models.IntegerField(null = False)
    posicion=models.CharField(max_length=50, choices= posiciones ,default="DESCONOCIDO")
    asistenciaComp=models.BooleanField(default=False)
    gym=models.BooleanField(default=False)
    amonestado=models.BooleanField(default=False)
    expulsado=models.BooleanField(default=False)
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)

class Entrenador(models.Model):
    nombre=models.CharField(max_length=25, default="")
    apellido=models.CharField(max_length=25, default="")
    dni=models.IntegerField(null = False)
    telefono=models.IntegerField(null = False)
    equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE)   

class Partido(models.Model):
    fecha = models.DateField(blank=False, primary_key=True)
    lugar = models.CharField(max_length=50)
    equipo_1 = models.ForeignKey('Equipo', on_delete= models.CASCADE, related_name = 'tuEquipo')
    equipo_2 = models.ForeignKey('Equipo', on_delete= models.CASCADE, related_name = 'OtroEquipo')
    numLine=models.IntegerField(blank=False)
    numScrum=models.IntegerField(blank=False)
    numPenales=models.IntegerField(blank=False)
    tri=models.IntegerField(blank=False)
    numConversiones=models.IntegerField(blank=False)
    numDrop=models.IntegerField(blank=False)
    numTacles=models.IntegerField(blank=False)
    numMaul=models.IntegerField(blank=False)
    numRuck=models.IntegerField(blank=False)
    cantPases=models.IntegerField(blank=False)
    
class Error(models.Model):
    numLinePerdidos=models.IntegerField(blank=False)
    numScrumPerdidos=models.IntegerField(blank=False)
    numPenalesEnContra=models.IntegerField(blank=False)
    numPelotasCaidas=models.IntegerField(blank=False)
    numConversionesErrados=models.IntegerField(blank=False)
    numTaclesErrados=models.IntegerField(blank=False)
    numPaseFoword=models.IntegerField(blank=False)
    numDropErrados=models.IntegerField(blank=False)
    numMaulErrados=models.IntegerField(blank=False)
    numRuckErrados=models.IntegerField(blank=False)

class Estadistica(models.Model):
    partido = models.ForeignKey('Partido', on_delete= models.CASCADE)
    error = models.ForeignKey('Error', on_delete= models.CASCADE)

    def porcLine (self):
        v = self.error.numLinePerdidos / self.partido.numLine
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcScrum (self):
        v = self.error.numScrumPerdidos / self.partido.numScrum
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcPenales (self):
        v = self.error.numPenalesEnContra / self.partido.numPenales
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcConver (self):
        v = self.error.numConversionesErrados / self.partido.numConversiones
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcDrop (self):
        v = self.error.numDropErrados / self.partido.numDrop
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcTacles (self):
        v = self.error.numTaclesErrados / self.partido.numTacles
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcPases (self):
        p = self.error.numPaseFoword + self.error.numPelotasCaidas
        v = p / self.partido.cantPases
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcRuck(self):
        v = self.error.numRuckErrados / self.partido.numRuck
        porc = int(v*100)
        porc = 100 - porc
        return porc

    def porcMaules(self):
        v = self.error.numMaulErrados / self.partido.numMaul
        porc = int(v*100)
        porc = 100 - porc
        return porc