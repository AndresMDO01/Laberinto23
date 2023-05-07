class Orientaciones:
    def ponerElementoEn(self, unaHab):
        pass

    def recorreEn(self,unBloque, unCont):
        pass

    def ir(alguien):
        pass




class Norte(Orientaciones):
    instancia = None

    def ponerElementoEn(self, unaHab, unEM):
        unaHab.norte = unEM

    def recorreEn(self,unBloque, unCont):
        unCont.norte.recorrer(unBloque)

    def ir(alguien):
        alguien.posicion.norte.entrar()

class Sur(Orientaciones):
    def ponerElementoEn(self, unaHab, unEM):
        unaHab.sur = unEM

    def recorreEn(self,unBloque, unCont):
        unCont.sur.recorrer(unBloque)

    def ir(alguien):
        alguien.posicion.sur.entrar()

class Este(Orientaciones):
    def ponerElementoEn(self, unaHab, unEM):
        unaHab.este = unEM

    def recorreEn(self, unBloque, unCont):
        unCont.este.recorrer(unBloque)

    def ir(alguien):
        alguien.posicion.este.entrar()


class Oeste(Orientaciones):
    def ponerElementoEn(self, unaHab, unEM):
        unaHab.oeste = unEM

    def recorreEn(self,unBloque, unCont):
        unCont.oeste.recorrer(unBloque)

    def ir(alguien):
        alguien.posicion.oeste.entrar()
