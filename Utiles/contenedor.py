class Contenedor:
    def __init__(self, id, nombre, imagen, cpu, ram):
        self.id = id
        self.nombre = nombre
        self.imagen = imagen
        self.cpu = int(cpu)
        self.ram = int(ram)
        self.estado = 'Activo'

    def mostrar_informacion(self):
        print(f"{self.id} | {self.nombre} | {self.imagen} | Estado: {self.estado}| CPU: {self.cpu} | Ram: {self.ram}GB")