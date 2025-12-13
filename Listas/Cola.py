from Listas.Nodo import Nodo

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.Longitud = 0

    def encolar(self, data):
        nuevo = Nodo(data)
        if self.frente is None:
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.Longitud += 1

    def desencolar(self):
        if self.frente is None:
            return None
        node = self.frente
        self.frente = node.siguiente
        if self.frente is None:
            self.final = None
        self.Longitud -= 1
        return node.data

    def esta_vacia(self):
        return self.frente is None