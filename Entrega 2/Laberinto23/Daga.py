from Decorator import Decorator

class Daga(Decorator):
    def __init__(self):
        super().__init__()

    def Forzar(self,unEM):
        print("Vas a usar la daga para forzar", unEM)
        unEM.cogerllave()




