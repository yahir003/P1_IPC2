import xml.etree.ElementTree as ET
from Centro import CentroDatos
from Utiles.Solicitud import Solicitudes

def cargar_xml(tipo):
    nombre_archivo = input(f"Ingrese el nombre del archivo XML de {tipo} (ejemplo: {tipo}.xml): ").strip()
    if nombre_archivo == '':
        return ''
    ruta_archivo = f'./entrada/{nombre_archivo}'
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8'):
         pass
        return ruta_archivo
    
    except Exception as e:
        print(f'archivo no encontrado: {ruta_archivo}')
        return ''

def leer_configuracion(ruta):
    if not ruta:
        print("Debe cargar primero el archivo XML")
        return
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        print(root.tag)

        if root.tag == 'cloudSync':

            # LEEENDO ETIQUETA CONFIGURACION
            configuracion = root.find('configuracion')
            if configuracion is not None:
                centros = configuracion.find('centrosDatos')
            if centros is not None:
                print('*' * 45)
                print("CENTROS DE DATOS:")
                    
            for centro in centros.findall('centro'):
                id = centro.get('id', '')
                nombre = centro.get('nombre', '')
                ubicacion = centro.find('ubicacion', '')
                pais = ubicacion.find('pais').text
                ciudad = ubicacion.find('ciudad').text
                capacidad = centro.find('capacidad')
                cpu = capacidad.find('cpu').text
                ram = capacidad.find('ram').text
                almacenamiento = capacidad.find('almacenamiento').text
                    
                print('* ' * 40)
                print('Centro De Datos')
                print('id: ', id)
                print('Nombre: ', nombre)
                print('Ciudad', ciudad)
                print('Cpu: ', cpu)
                print('Ram :', ram)
                print('Almacenamiento: ', almacenamiento)

            # LEEENDO ETIQUETA MAQUINAS VIRTUALES

            vms = configuracion.find('maquinasVirtuales')
            if vms is not None:
                print('*' * 45)
            print("MAQUINAS VIRTUALES:")

            for vm in vms.findall('vm'):
                vm_id = vm.get('id', '')
                centro_asignado = vm.get('centroAsignado', '')
                so = vm.find('sistemaOperativo').text
                recursos = vm.find('recursos')
                cpu = recursos.find('cpu').text
                ram = recursos.find('ram').text
                almacenamiento = recursos.find('almacenamiento').text
                ip = vm.find('ip').text

                print('* ' * 45)
                print('Maquina Virtual')
                print('ID: ', vm_id)
                print('Centro Asignado: ', centro_asignado)
                print('Sistema Operativo: ', so)
                print('CPU: ', cpu)
                print('RAM: ', ram)
                print('Almacenamiento: ', almacenamiento)
                print('Ip: ', ip)

        solicitudes = configuracion.find('solicitudes')
        if solicitudes is not None: 
            print(*'=' * 45)
            print("SOLICITUDES:")
            
            for sol in solicitudes.findall('solicitud'):
                sol_id = sol.get('id', '')
                cliente = sol.find('cliente').text
                tipo = sol.find('tipo').text
                prioridad = sol.find('prioridad').text
                recursos = sol.find('recursos')
                cpu = recursos.find('cpu').text
                ram = recursos.find('ram').text
                almacenamiento = recursos.find('almacenamiento').text
                tiempo = sol.find('tiempoEstimado').text

                print('* ' * 45)
                print('Solicitud')
                print('ID', sol_id)
                print('Cliente: ', cliente)
                print('Tipo: ', tipo)
                print('Prioridad: ', prioridad)
                print('CPU: ', cpu)
                print('RAM :', ram)
                print('Almacenamiento: ', almacenamiento)
                print('Tiempo Estimado: ', tiempo)

        # LEENDO ETIQUETA INSTRUCCIONES
        instucciones = root.find('instrucciones')
        if instucciones is not None:
            print('*' * 45)
            print('INSTRUCCIONES:')

            for instruccion in instucciones.findall('instruccion'):
                tipo = instruccion.get('tipo', '')

                print('* ' * 45)
                print('Instruccion')
                print('Tipo: ', tipo)

                if tipo == "crearVM":
                    inst_id = instruccion.find('id').text
                    centro = instruccion.find('centro').text
                    so = instruccion.find('so').text
                    cpu = instruccion.find('cpu').text
                    ram = instruccion.find('ram').text
                    almacenamiento = instruccion.find('almacenamiento').text

                    print('ID:', inst_id)
                    print('Centro Asignado:', centro)
                    print('SO:', so)
                    print('CPU:', cpu)
                    print('RAM:', ram)
                    print('Almacenamiento:', almacenamiento)

                elif tipo == "migrarVM":
                    vm_id = instruccion.find('vmId').text
                    origen = instruccion.find('centroOrigen').text
                    destino = instruccion.find('centroDestino').text

                    print('VM ID:', vm_id)
                    print('Centro Origen:', origen)
                    print('Centro Destino:', destino)

                elif tipo == "procesarSolicitudes":
                    cantidad = instruccion.find('cantidad').text
                    print('Cantidad:', cantidad)

    except Exception as e:
        print(f"Error al leer configuracion: {e}")


ruta = cargar_xml("configuracion")
leer_configuracion(ruta)


def cargar_centros_desde_xml(ruta, lista_centros):
    tree = ET.parse(ruta)
    root = tree.getroot()

    configuracion = root.find('configuracion')
    centros = configuracion.find('centrosDatos')

    for centro in centros.findall('centro'):
        id = centro.get('id')
        capacidad = centro.find('capacidad')

        cpu = int(capacidad.find('cpu').text)
        ram = int(capacidad.find('ram').text)
        almacenamiento = int(capacidad.find('almacenamiento').text)

        nuevo_centro = CentroDatos(id, cpu, ram, almacenamiento)
        lista_centros.insertar(nuevo_centro)

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

        

def cargar_solicitudes_desde_xml(ruta, lista_solicitudes, cola_solicitudes):
    tree = ET.parse(ruta)
    root = tree.getroot()

    configuracion = root.find('configuracion')
    solicitudes = configuracion.find('solicitudes')

    if solicitudes is None:
        return

    for sol in solicitudes.findall('solicitud'):
        sol_id = sol.get('id')
        cliente = sol.find('cliente').text
        tipo = sol.find('tipo').text
        prioridad = sol.find('prioridad').text
        recursos = sol.find('recursos')

        cpu = recursos.find('cpu').text
        ram = recursos.find('ram').text
        almacenamiento = recursos.find('almacenamiento').text
        tiempo = sol.find('tiempoEstimado').text

        nueva = Solicitudes(
            sol_id, cliente, tipo, prioridad,
            cpu, ram, almacenamiento, tiempo
        )

        lista_solicitudes.insertar(nueva)
        cola_solicitudes.insertar(nueva)

