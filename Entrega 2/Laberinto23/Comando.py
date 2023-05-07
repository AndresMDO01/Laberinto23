class Comando:
    def __int__(self):
        self.receptor

    def ejecutar(self):
        pass

    def esForzar(self):
        return False

class Forzar(Comando):
    def ejecutar(self, unEM):
        print("Estas forzando un EM para abrirlo")
        unEM.cogerllave()

    def esForzar(self):
        return True


class Reventar(Comando):
    def ejecutar(self, unEM):
        print("Has reventado un EM para abrirlo")
        unEM.cogerllave()

    def esReventar(self):
        return True