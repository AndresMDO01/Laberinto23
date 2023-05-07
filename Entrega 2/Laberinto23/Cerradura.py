from Decorator import Decorator
class Cerradura(Decorator):

    def __init__(self):
        super().__init__()
        self.llave = False

    def entrar(self):
        if (self.llave == True):
            self.component.abrir()
            self.component.entrar()
        else:
            print(str(self.component) + " tiene una cerradura, ingeniatelas para abrir este elemenento del mapa")


    def cogerllave(self):
        self.llave = True


    #Estos métodos los propongo como solución para poder combinar el iterator y el decorator
    def esPuerta(self):
        return self.component.esPuerta()

    def abrir(self):
        if (self.llave == True):
            return self.component.abrir()
        else:
            return False



