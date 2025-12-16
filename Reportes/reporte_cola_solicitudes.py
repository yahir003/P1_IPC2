from graphviz import Digraph
import os

def reporte_cola(cola):
    dot = Digraph("ColaSolicitudes", format="png")
    dot.attr(rankdir="LR")

    actual = cola.primero
    prev = None
    i = 1

    if actual is None:
        dot.node("vacia", "Cola vacía", shape="box")
    else:
        while actual:
            s = actual.dato
            nombre = f"N{i}"
            dot.node(
                nombre,
                f"Solicitud {s.id}\nPrioridad: {s.prioridad}",
                shape="box",
                style="filled",
                fillcolor="lightcoral"
            )

            if prev:
                dot.edge(prev, nombre)

            prev = nombre
            actual = actual.siguiente
            i += 1

    os.makedirs("Reportes/salidas", exist_ok=True)
    dot.render("Reportes/salidas/cola_solicitudes")

    print("Reporte generado: cola_solicitudes.png")
