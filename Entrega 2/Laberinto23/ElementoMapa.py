class ElementoMapa:
    # Constructor de la clase
    def __init__(self):
        self.padre = None
        self.comandos = []
    
    def entrar (self):
        pass

    def recorrer(self,unBloque):
        unBloque(self)

    def esPuerta(self):
        return False

    def esBomba(self):
        return False

    def agregarComando(self, unComando):
        self.comandos.append(unComando)

    def quitarComando(self,unComando):
        if unComando in self.comandos:
            self.comandos.remove(unComando)

    # Añadimos este método para que al hacer la llamada desde Cerradura no nos muestre la referencia
    def __str__(self):
        return str(type(self).__name__)
