from ElementoMapa import ElementoMapa

class Decorator(ElementoMapa):
    def __init__(self):
        super().__init__()
        self.component = None

    def component(self, component):
        self.component = component