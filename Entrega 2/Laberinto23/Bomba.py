from Decorator import Decorator

class Bomba(Decorator):

    def __init__(self):
        super().__init__()
        self.activa = False

    def entrar(self):
        if (self.activa == True):
            print("PUM pa tu casa")
            print("La partida ha terminado")
        else:
            self.component.entrar()

    def esBomba(self):
        return True

    def activarBomba(self):
        self.activa = True

    def desactivarBomba(self):
        self.activa = False

    def Reventar(self,unEM):
        print("Vas a usar la bomba para reventar", unEM)
        unEM.cogerllave()

    #Estos métodos los propongo como solución para poder combinar el iterator y el decorator
    def esPuerta(self):
        if self.component != None: #Bomba puede ser un decorador o ponerlo como un hijo de un contenedor.
            return self.component.esPuerta()

    def abrir(self):
        return self.component.abrir()

