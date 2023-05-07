from Contenedor import Contenedor

class Laberinto(Contenedor):
    def __init__(self, norte=None, sur=None, este=None, oeste=None):
        super().__init__(num=None, norte=norte, sur=sur, este=este, oeste=oeste)

    def agregarHabitacion(self,unHab):
        self.agregarHijo(unHab)
