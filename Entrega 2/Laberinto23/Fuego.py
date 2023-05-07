import time

from Decorator import Decorator
class Fuego(Decorator):

    def __init__(self):
        super().__init__()

    def entrar(self):
            print("Te has dejado el gas puesto y la habitación....ESTA EN LLAMAS")
            time.sleep(3)
            print("TE ESTAS QUEMANDO")
            time.sleep(5)
            print("Ohh!! Te has muerto :( ")
            print("La partida ha terminado")


