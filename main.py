from Listas.Listasimple import ListaSimple
from gestion_centros import menu_centros
from lectorxml import cargar_xml, cargar_centros_a_lista

def main():
    lista_centros = ListaSimple()
    ruta = ''

    while True:
        print(('*'*20)+'CONTROL CENTRO DE DATOS'+('*'*20))
        print('1. Cargar XML')
        print('2. Gestion de centros')
        print('3. Salir')

        op = input('Seleccione un Opcion: ')

        if op == '1':
            ruta = cargar_xml('configuracion')
            if ruta:
                cargar_centros_a_lista(ruta, lista_centros)
                print('XML cargado correctamente')

        elif op == '2':
            menu_centros(lista_centros)

        elif op == '3':
            break

main()
