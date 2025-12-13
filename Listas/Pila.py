from Listas.Nodo import Nodo

class Pila:
    def __init__(self):
        self.arriba = None 
        self.longitud = 0
    
    def insertar(self, data):
        nuevo = Nodo(data)
        nuevo.siguiente = self.arriba
        self.arriba = nuevo
        self.longitud += 1

    def eliminar(self):
        if self.arriba is None:
            return None
        node = self.top
        self.arriba = node.siguiente
        self.longitud -= 1
        return node.data
    
    def estavacia(self):
        return self.arriba is None