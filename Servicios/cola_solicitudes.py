from Listas.Listasimple import Nodo

class ColaSolicitudes:
    def __init__(self):
        self.primero = None

    def insertar(self, solicitud):
        nuevo = Nodo(solicitud)

        # Cola vacía
        if self.primero is None:
            self.primero = nuevo
            return

        # Mayor prioridad primero
        if solicitud.prioridad > self.primero.dato.prioridad:
            nuevo.siguiente = self.primero
            self.primero = nuevo
            return

        actual = self.primero
        while (actual.siguiente and
               actual.siguiente.dato.prioridad >= solicitud.prioridad):
            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def mostrar(self):
        if self.primero is None:
            print("No hay solicitudes en cola")
            return

        print("COLA DE SOLICITUDES (Mayor → Menor prioridad)")
        actual = self.primero
        while actual:
            actual.dato.mostrar_info()
            actual = actual.siguiente
