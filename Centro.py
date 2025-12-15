import xml.etree.ElementTree as ET
from Listas.Listasimple import ListaSimple


class CentroDatos:
    def __init__(self, id, cpu, ram, almacenamiento):
        self.id = id

        self.cpu_total = int(cpu)
        self.ram_total = int(ram)
        self.alm_total = int(almacenamiento)
        self.cpu_disponible = int(cpu)
        self.ram_disponible = int(ram)
        self.alm_disponible = int(almacenamiento)
        self.vms_activas = 0

        self.lista_vms = ListaSimple()

    def mostrar_info(self):
        cpu_usado = self.cpu_total - self.cpu_disponible
        ram_usado = self.ram_total - self.ram_disponible
        alm_usado = self.alm_total - self.alm_disponible

        print('*' * 45)
        print('Centro ID:', self.id)
        print('CPU Total:', self.cpu_total, '| CPU Disponible:', self.cpu_disponible, '| CPU Usado:', cpu_usado)
        print('RAM Total:', self.ram_total, '| RAM Disponible:', self.ram_disponible, '| RAM Usada:', ram_usado)
        print('Almacenamiento Total:', self.alm_total, '| Disponible:', self.alm_disponible, '| Usado:', alm_usado)
        print('Vms Activas:', self.vms_activas)

        cpu_p = (cpu_usado * 100) / self.cpu_total
        print(f'CPU usada (%): {cpu_p:.2f}%')
        print('*' * 40)

    def cargar_centros_a_lista(ruta, lista_centros):
        tree = ET.parse(ruta)
        root = tree.getroot()

        configuracion = root.find('configuracion')
        if configuracion is None:
            return

        centros = configuracion.find('centrosDatos')
        if centros is None:
            return

        for c in centros.findall('centro'):
            id = c.get('id')
            capacidad = c.find('capacidad')

            cpu = int(capacidad.find('cpu').text)
            ram = int(capacidad.find('ram').text)
            almacenamiento = int(capacidad.find('almacenamiento').text)

            centro = CentroDatos(id, cpu, ram, almacenamiento)
            lista_centros.insertar(centro)

    
    def buscar_vm(self, vm_id):
        actual = self.lista_vms.primero
        while actual:
            if actual.dato.id == vm_id:
                return actual.dato
            actual = actual.siguiente
        return None
