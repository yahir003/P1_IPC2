from Listas.Listasimple import ListaSimple
from gestion_centros import menu_centros
from Servicios.gestion_mavi import menu_mavi
from lectorxml import cargar_xml, cargar_centros_a_lista
from Utiles.maquina_virtual import cargar_mv_a_lista
from Servicios.gestion_contenedor import menu_conte

def main():
    lista_centros = ListaSimple()
    lista_vms = ListaSimple()
    ruta = ''

    while True:
        print(('*'*20)+'CONTROL CENTRO DE DATOS'+('*'*20))
        print('1. Cargar XML')
        print('2. Gestion de centros de datos')
        print('3. Gestion de maquinas virtuales')
        print('4. Gestion de contenedores')
        print('5. Gestion de solicitudes')
        print('6. Reportes graphviz')
        print('7. Generador XML de salida')
        print('8. Historial de operaciones')
        print('9. Salir')

        op = input('Seleccione un Opcion: ')

        if op == '1':
            ruta = cargar_xml('configuracion')
            if ruta:
                cargar_centros_a_lista(ruta, lista_centros)
                cargar_mv_a_lista(ruta, lista_vms)
                print('XML cargado correctamente')

        elif op == '2':
            menu_centros(lista_centros)

        elif op == '3':
            menu_mavi(lista_vms, lista_centros)

        elif op == '4':
            menu_conte(lista_vms)
        
        elif op == '5':
            print("en espera")
        
        elif op == '6':
            print("en espera")
        
        elif op == '7':
            print("en espera")

        elif op == '8':
            print("en espera")

        elif op == '9':
            print('Saliendo del programa....')
            break

        else:
            print('Opcion no valida intente de nuevo...')

main()
