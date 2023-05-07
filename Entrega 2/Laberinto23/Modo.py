class Modo:
    def actua(self):
        pass
    def caminar(self):
        pass
    def dormir(self):
        pass
    def esAgresivo(self):
        return False
    def esPerezoso(self):
        return False

class Agresivo(Modo):
    def esAgresivo(self):
        return True

class Perezoso(Modo):
    def esPerezoso(self):
        return True