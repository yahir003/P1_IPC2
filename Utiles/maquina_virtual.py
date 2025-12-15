from Listas.Listasimple import ListaSimple
import xml.etree.ElementTree as ET

class Maquinavirtual:
    def __init__(self, id, sistema, cpu, ram, almacenamiento, centro_id, ip):
        self.id = id
        self.sistema = sistema
        self.cpu = int(cpu)
        self.ram = int(ram)
        self.almacenamiento = int(almacenamiento)
        self.centro_id = centro_id
        self.ip = ip

        self.cpu_usado = 0
        self.ram_usado = 0
        self.contenedor = ListaSimple()
        self.estado = 'Activo'

    def mostrar_info(self):
        print('*' * 45)
        print('ID VM', self.id)
        print('Sistema operativo', self.sistema, '(CPU: ',self.cpu, 'RAM: ',self.ram,'GB)')
        print('Estado', self.estado)
        print('IP: ',self.ip)
        print('Centro', self.centro_id)
        print('Contenedores: ',self.contenedor.contar())
        print('Almacenamiento', self.almacenamiento)
    
    def mostrar_general_vm(self, numero):
        print(f"\n{numero}. VM: {self.id} - {self.sistema} (CPU: {self.cpu}, RAM: {self.ram}GB)")
        print(f"   Estado: {self.estado}")
        print(f"   IP: {self.ip}")
        print(f"   Contenedores: {self.contenedor.contar()}")

def cargar_mv_a_lista(ruta, lista_vms):
    tree = ET.parse(ruta)
    root = tree.getroot()

    configuracion = root.find('configuracion')
    if configuracion is None:
        return
    
    vms = configuracion.find('maquinasVirtuales')
    if vms is None:
        return
    
    for vm in vms.findall('vm'):
        vm_id = vm.get('id')
        centro_asignado = vm.get('centroAsignado')

        sistema = vm.find('sistemaOperativo').text

        recursos = vm.find('recursos')
        cpu = recursos.find('cpu').text
        ram = recursos.find('ram').text
        almacenamiento = recursos.find('almacenamiento').text

        ip = vm.find('ip').text

        nueva_vm = Maquinavirtual(vm_id, sistema, cpu, ram, almacenamiento, centro_asignado, ip)

        lista_vms.insertar(nueva_vm)

