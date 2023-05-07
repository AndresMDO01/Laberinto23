from Contenedor import Contenedor

class Habitacion(Contenedor):
    
    def __init__(self, num, norte=None, sur=None, este=None, oeste=None):
        super().__init__(num, norte, sur, este, oeste)
        
    def entrar(self):
        print("Estas en la habitación", self.num)

    
    
