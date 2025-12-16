from Listas.Listasimple import ListaSimple
from gestion_centros import menu_centros
from Servicios.gestion_mavi import menu_mavi
from Servicios.gestion_contenedor import menu_conte
from Servicios.gestion_solicitud import menu_solicitudes
from lectorxml import cargar_xml, cargar_centros_a_lista, cargar_solicitudes_desde_xml
from Utiles.maquina_virtual import cargar_mv_a_lista

def main():
    lista_centros = ListaSimple()
    lista_vms = ListaSimple()
    lista_solicitudes = ListaSimple()
    ruta = ''

    while True:
        print('*' * 20 + 'CONTROL CENTRO DE DATOS' + '*' * 20)
        print('1. Cargar XML')
        print('2. Gestion de centros de datos')
        print('3. Gestion de maquinas virtuales')
        print('4. Gestion de contenedores')
        print('5. Gestion de solicitudes')
        print('6. Salir')

        op = input('Seleccione una opcion: ')

        if op == '1':
            ruta = cargar_xml('configuracion')
            if ruta:
                cargar_centros_a_lista(ruta, lista_centros)
                cargar_mv_a_lista(ruta, lista_vms)
                cargar_solicitudes_desde_xml(ruta, lista_solicitudes)
                print("XML cargado correctamente")

        elif op == '2':
            menu_centros(lista_centros)

        elif op == '3':
            menu_mavi(lista_vms, lista_centros)

        elif op == '4':
            menu_conte(lista_vms)

        elif op == '5':
            menu_solicitudes(lista_solicitudes, lista_centros)

        elif op == '6':
            print("Saliendo...")
            break

        else:
            print("Opción inválida")

main()
