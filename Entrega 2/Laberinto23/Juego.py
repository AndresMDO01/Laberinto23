from Laberinto import Laberinto
from Habitacion import Habitacion
from Orientaciones import Norte, Sur, Este, Oeste
from Bicho import Bicho
from Modo import Agresivo, Perezoso
from Pared import Pared
from Puerta import Puerta
from Armario import Armario
from Bomba import Bomba
from Cerradura import Cerradura
from Fuego import Fuego
from Baul import Baul
from Daga import Daga
class Juego:
    
    def __init__(self):
        self.laberinto = None
        self.bichos = []

    #MÉTODOS DE FABRICACIÓN

    def fabricarLaberinto(self):
        return Laberinto()
    
    def fabricarNorte(self):
        return Norte()
    
    def fabricarSur(self):
        return Sur()
    
    def fabricarEste(self):
        return Este()
    
    def fabricarOeste(self):
        return Oeste()
    
    def fabricarPared(self):
        return Pared()
    
    def fabricarHabitacion(self,unNum):
        hab = Habitacion(unNum)
        hab.ponerEnElemento(self.fabricarNorte(), self.fabricarPared())
        hab.ponerEnElemento(self.fabricarSur(), self.fabricarPared())
        hab.ponerEnElemento(self.fabricarEste(), self.fabricarPared())
        hab.ponerEnElemento(self.fabricarOeste(), self.fabricarPared())

        hab.agregarOrientaciones(self.fabricarNorte())
        hab.agregarOrientaciones(self.fabricarSur())
        hab.agregarOrientaciones(self.fabricarEste())
        hab.agregarOrientaciones(self.fabricarOeste())
        
        return hab
    
    def fabricarPuerta(self, unHab, otraHab):
        return Puerta(unHab, otraHab)

    def agregarBicho(self,unBicho):
        self.bichos.append(unBicho)

    def fabricarBichoAgresivoEn(self, unaPosicion):
        bicho = Bicho(10, 10, unaPosicion, self.fabricarModoAgresivo())
        return bicho

    def fabricarBichoPerezosoEn(self, unaPosicion):
        bicho = Bicho(10, 10, unaPosicion, self.fabricarModoPerezoso())
        return bicho

    def fabricarArmarioEn(self, unCont):
        unNuM = (len(unCont.hijos)) + 1
        arm = Armario(unNuM)
        arm.ponerEnElemento(self.fabricarNorte(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarSur(),self.fabricarPuerta(unCont,arm))
        arm.ponerEnElemento(self.fabricarEste(),self.fabricarPared())
        arm.ponerEnElemento(self.fabricarOeste(),self.fabricarPared())

        arm.agregarOrientaciones(self.fabricarNorte())
        arm.agregarOrientaciones(self.fabricarSur())
        arm.agregarOrientaciones(self.fabricarEste())
        arm.agregarOrientaciones(self.fabricarOeste())

        return arm
    
    def fabricarModoAgresivo(self):
        return Agresivo()

    def fabricarModoPerezoso(self):
        return Perezoso()


    def fabricarBomba(self):
        return Bomba()

    def fabricarCerradura(self):
        return Cerradura()

    def fabricarFuego(self):
        return Fuego()

    def fabricarBaulEn(self, unCont):
        unNuM = (len(unCont.hijos)) + 1
        baul = Baul(unNuM)
        unCont.agregarHijo(baul)
        return baul

    def fabricarDaga(self):
        return Daga()

    def laberinto2HabitacionesFM(self):


        self.laberinto = self.fabricarLaberinto()


        "HABITACIONES"
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)


        "PUERTAS"
        p12 = self.fabricarPuerta(hab1, hab2)
        hab1.ponerEnElemento(self.fabricarSur(), p12)
        hab2.ponerEnElemento(self.fabricarNorte(), p12)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)

        "ARMARIO"
        arm1=self.fabricarArmarioEn(hab1)
        hab1.ponerEnElemento(self.fabricarNorte(),arm1)

        "BICHOS"
        bicho1 = self.fabricarBichoAgresivoEn(hab1)
        bicho2 = self.fabricarBichoPerezosoEn(hab2)

        self.agregarBicho(bicho1)
        self.agregarBicho(bicho2)

        return self.laberinto


    def laberinto4Habitaciones(self):

        self.laberinto = self.fabricarLaberinto()

        "HABITACIONES"
        hab1 = self.fabricarHabitacion(1)
        hab2 = self.fabricarHabitacion(2)
        hab3 = self.fabricarHabitacion(3)
        hab4 = self.fabricarHabitacion(4)


        "PUERTAS"
        p12=self.fabricarPuerta(hab1,hab2)
        hab1.ponerEnElemento(self.fabricarEste(),p12)
        hab2.ponerEnElemento(self.fabricarOeste(),p12)

        cerr1 = self.fabricarCerradura()
        cerr1.component = self.fabricarPuerta(hab1, hab3)
        hab1.ponerEnElemento(self.fabricarSur(), cerr1)
        hab3.ponerEnElemento(self.fabricarNorte(), cerr1)

        bm1 = self.fabricarBomba()
        bm1.component = self.fabricarPuerta(hab3, hab4)
        hab3.ponerEnElemento(self.fabricarEste(), bm1)
        hab4.ponerEnElemento(self.fabricarOeste(), bm1)


        p24 = self.fabricarPuerta(hab1, hab3)
        hab2.ponerEnElemento(self.fabricarSur(), p24)
        hab4.ponerEnElemento(self.fabricarNorte(), p24)

        #Añadimos el decorador fuego una vez que se ha construido el laberinto
        #ya que si lo ponemos antes no podemos construir la habitación hab4 por falta de métodos en Fuego

        f1 = self.fabricarFuego()
        f1.component = hab4
        hab4 = f1

        "BAULES"
        b1 = self.fabricarBaulEn(hab2)
        bm2 = self.fabricarBomba()
        b1.agregarHijo(bm2)
        daga = self.fabricarDaga()
        "Vemos que daga no decora sino que se añade como hijo"
        b2 = self.fabricarBaulEn(hab3)
        b2.agregarHijo(daga)

        self.laberinto.agregarHabitacion(hab1)
        self.laberinto.agregarHabitacion(hab2)
        self.laberinto.agregarHabitacion(hab3)
        self.laberinto.agregarHabitacion(hab4)

        return self.laberinto


    #MÉTODOS AUXILIARES

    def abrirPuertas(self):
        self.laberinto.recorrer(lambda each:each.abrir() if each.esPuerta() else None)

    def activarBombas(self):
        self.laberinto.recorrer(lambda each:each.activarBomba() if each.esBomba() else None)

    def desactivarBombas(self):
        self.laberinto.recorrer(lambda each:each.desactivarBomba() if each.esBomba() else None)

        self.fabricarBomba().entrar()

