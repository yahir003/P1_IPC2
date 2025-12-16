class Solicitudes:
    def __init__(self, id, cliente, tipo, prioridad, cpu, ram, almacenamiento, tiempo):
        self.id = id
        self.cliente = cliente
        self.tipo = tipo
        self.prioridad = int(prioridad)
        self.cpu = int(cpu)
        self.ram = int(ram)
        self.almacenamiento = int(almacenamiento)
        self.tiempo = int(tiempo)

    def mostrar_info(self):
        print("*" * 40)
        print("ID:", self.id)
        print("Cliente:", self.cliente)
        print("Tipo:", self.tipo)
        print("Prioridad:", self.prioridad)
        print("CPU:", self.cpu)
        print("RAM:", self.ram)
        print("Almacenamiento:", self.almacenamiento)
        print("Tiempo estimado:", self.tiempo)
  