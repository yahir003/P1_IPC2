from graphviz import Digraph
import os

def reporte_centros(lista_centros):
    dot = Digraph("Centros", format="png")
    dot.attr(rankdir="LR")

    actual = lista_centros.primero

    while actual:
        c = actual.dato
        dot.node(
            c.id,
            f"Centro {c.id}\nCPU:{c.cpu_disponible}/{c.cpu_total}\nRAM:{c.ram_disponible}/{c.ram_total}",
            shape="box",
            style="filled",
            fillcolor="lightgreen"
        )
        actual = actual.siguiente

    os.makedirs("Reportes/salidas", exist_ok=True)
    dot.render("Reportes/salidas/centros")

    print("Reporte generado: centros.png")
