from Contenedor import Contenedor
class Baul(Contenedor):
    def abrir(self):
        print("Has abierto el baúl y este baúl contiene:")
        for i in range(len(self.hijos)):
            print(str(self.hijos[i]))

    def coger(self, unNum):
        return self.hijos[unNum]