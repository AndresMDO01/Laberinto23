from Contenedor import Contenedor

class Armario(Contenedor):
    def entrar(self):
        print("Has entrado en el armario", self.num)
        