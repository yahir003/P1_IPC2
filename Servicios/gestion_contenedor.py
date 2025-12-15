from Utiles.contenedor import Contenedor

def desplegar(lista_vms):
    print('------Despliege de contenedores------')
    id_vm = input('Ingrese el ID del VM donde se alogara el contenedor: ').strip()

    nodo_actual = lista_vms.primero
    vm_encontrado = None

    while nodo_actual:
        if nodo_actual.dato.id == id_vm:
            vm_encontrado = nodo_actual.dato
            break
        nodo_actual = nodo_actual.siguiente

    if vm_encontrado is None:
        print('No se encontro la VM con el id ')
        return
    
    cpu_libre = vm_encontrado.cpu - vm_encontrado.cpu_usado
    ram_libre = vm_encontrado.ram - vm_encontrado.ram_usado
    
    print(f"Vm Seleccionado: {vm_encontrado.sistema}")
    print(f"Capacidad disponible: Cpu{cpu_libre}, Ram:{ram_libre}GB")
    print('------Ingrese los datos requeridos------')
    cont_id = input('ID del nuevo contenedor: ')
    nombre = input('Nombre del contenedor: ')
    imagen = input('iamgen del contenedor: ')
    cpu = int(input('CPU requerida: '))
    ram = int(input('RAM requerida: '))

    if cpu <= cpu_libre and ram <= ram_libre:
        nuevo_contenedor = Contenedor(cont_id, nombre, imagen, cpu, ram)
        vm_encontrado.contenedor.insertar(nuevo_contenedor)

        vm_encontrado.cpu_usado += cpu
        vm_encontrado.ram_usado += ram

        print(f" Exito contenedor: '{nombre}' desplegao en: '{id_vm}")
        print(f"Recursos Vm usados: {vm_encontrado.cpu_usado}/{vm_encontrado.cpu}")
    else:
        print('Error recursos insuficientes')
        print(f" Requerimiento: CPU {cpu}, RAM: {ram}")
        print(f" Disponibles: CPU {cpu_libre}, RAM: {ram_libre}")

def listas_contenedores(lista_vms):
    print('------Listas de contenedores------')
    id_vm = input('Ingrese el ID del VM para ver: ').strip()

    nodo_actual = lista_vms.primero
    vm_encontrado = None

    while nodo_actual:
        if nodo_actual.dato.id == id_vm:
            vm_encontrado = nodo_actual.dato
            break
        nodo_actual = nodo_actual.siguiente

    if vm_encontrado is None:
        print('No se encontro la VM con el id ')
        return
    if vm_encontrado.contenedor.primero is None:
        print('No tiene contenedores desplegados')
        return
    
    nodo_cont = vm_encontrado.contenedor.primero
    while nodo_cont:
        c = nodo_cont.dato
        print(f"Contenedor: {c.id:<10} - {c.nombre:<10} - {c.imagen:<10}")
        print(f"Estado: {c.estado}")
        print(f"CPU: {c.cpu}%")
        print(f"Ram: {c.ram}MB")
        nodo_cont = nodo_cont.siguiente
        print('----------------------------------------------')

def cambiar_estado(lista_vms):
    id_vm = input('Ingrese el ID del VM para ver: ').strip()

    nodo_vm = lista_vms.primero
    vm_encontrado = None

    while nodo_vm:
        if nodo_vm.dato.id == id_vm:
            vm_encontrado = nodo_vm.dato
            break
        nodo_vm = nodo_vm.siguiente

    if vm_encontrado is None:
        print('No se encontro la VM con el id ')
        return
    id_cont = input('Ingrese el ID del contenedor: ').strip()

    nodo_cont = vm_encontrado.contenedor.primero
    cont_encontrado = None

    while nodo_cont:
        if nodo_cont.dato.id == id_cont:
            cont_encontrado = nodo_cont.dato
            break
        nodo_cont = nodo_cont.siguiente
    
    if cont_encontrado is None:
        print('Error el contenedor no exite en la VM')
        return
    
    estado_actual = cont_encontrado.estado
    print(f"Contenedor: {cont_encontrado.nombre}")
    print(f"Estado actual: {estado_actual}")
    print('---------------------------')
    print('1. Activo')
    print('2. Pausa')
    print('3. Detenido')
    print('4. Cancelar')

    opcion_estado = input('selecciones un estado: ')
    nuevo_estado = ""

    if opcion_estado == '1':
        nuevo_estado = 'Activo'
    elif opcion_estado == '2':
        nuevo_estado = 'Pausado'
    elif opcion_estado == '3':
        nuevo_estado = 'Detenido'
    elif opcion_estado == '4':
        print('Operacion cancelada')
        return
    else:
        print('Opcion no valida escoga ne nuevo....')
        return
    
    if estado_actual == nuevo_estado:
        print('El contenedor ya se encuentra en el estado: ', {nuevo_estado})
        return

    if estado_actual == 'Detenido' and nuevo_estado == 'Pausado':
        print('Error no se puede pausar un contenedor detenido')
        return
    
    cont_encontrado.estado = nuevo_estado
    print('Exito el estado del contenedor se cambio a: ', {nuevo_estado})

def Eliminacion(lista_vms):
    id_vm = input('Ingrese el ID del VM para ver: ').strip()

    nodo_vm = lista_vms.primero
    vm_encontrado = None

    while nodo_vm:
        if nodo_vm.dato.id == id_vm:
            vm_encontrado = nodo_vm.dato
            break
        nodo_vm = nodo_vm.siguiente

    if vm_encontrado is None:
        print('No se encontro la VM con el id ')
        return
    
    id_cont = input('Ingrese el ID del contenedor: ').strip()

    actual = vm_encontrado.contenedor.primero
    anterior = None
    encontrado = False

    while actual:
        if actual.dato.id == id_cont:
            datos_cont = actual.dato

            vm_encontrado.cpu_usado -= datos_cont.cpu
            vm_encontrado.ram_usado -= datos_cont.ram

            if vm_encontrado.cpu_usado < 0: vm_encontrado.cpu_usado = 0
            if vm_encontrado.ram_usado < 0: vm_encontrado.ram_usado = 0

            if anterior is None:
                vm_encontrado.contenedor.primero = actual.siguiente
            else:
                anterior.siguiente = actual.siguiente

            encontrado = True
            print(f"Exito el contenedor fue eliminado")
        anterior = actual
        actual = actual.siguiente

    if not encontrado:
        print(f"Error el contenedor '{id_cont}' no se encontro en '{id_vm}'")

def menu_conte(lista_vms):
    while True:
        print('*'*20,'  Gestion de contendores  ','*'*20)
        print('1. Desplegar contenedor en VM')
        print('2. Listar contenedores de una VM')
        print('3. Cambiar estado de un contenedor')
        print('4. Eliminar contenedor')
        print('5. Volver al menu principal')

        op = input('Seleccione una Opcion: ')

        if op == '1':
            desplegar(lista_vms)
        elif op == '2':
            listas_contenedores(lista_vms)
        elif op == '3':
            cambiar_estado(lista_vms)
        elif op == '4':
            Eliminacion(lista_vms)
        elif op == '5':
            break
        else:
            print('Opcion no valida intente de nuevo...')