from ElementoMapa import ElementoMapa
class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 =  lado2
        self.abierta = False

    def abrir(self):
        self.abierta = True
    
    def cerrar(self):
        self.abierta = False
    
    def entrar(self):
        if (self.abierta == False): print("La puerta esta cerrada")
        else:
            print("La puerta esta abierta")

    def esPuerta(self):
        return True

    def abrir(self):
        self.abierta = True

    def cerrar(self):
        self.abierta = False



