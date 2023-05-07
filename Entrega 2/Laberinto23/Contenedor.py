from ElementoMapa import ElementoMapa
from Orientaciones import Orientaciones

class Contenedor(ElementoMapa):

    def __init__(self,num = None, norte = None, sur=None, este=None, oeste=None):
        super().__init__()
        self.hijos = []
        self.num = num 
        self.norte = norte
        self.sur = sur
        self.este = este
        self.oeste = oeste
        self.orientaciones = []

    def agregarHijo(self, unEM):
        self.hijos.append(unEM)
        unEM.padre = self

    def agregarOrientaciones(self, unaOr):
        self.orientaciones.append(unaOr)

    def ponerEnElemento(self, unaOr, unEM):
        if isinstance(unaOr,Orientaciones):    
            unaOr.ponerElementoEn(self, unEM)

        else:
            raise ValueError('unaOr debe ser una instancia de Orientaciones')

    def recorrer(self,unBloque):
        unBloque(self)
        for each in self.hijos:
            each.recorrer(unBloque)

        for each in self.orientaciones:
            each.recorreEn(unBloque,self)