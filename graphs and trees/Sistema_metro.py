from collections import deque
metro = {
    "Portal Norte":   ["Toberín"],
    "Toberín":        ["Portal Norte", "Calle 142"],
    "Calle 142":      ["Toberín", "Calle 127"],
    "Calle 127":      ["Calle 142", "Pepe Sierra", "Alcalá"],
    "Pepe Sierra":    ["Calle 127", "Niza"],
    "Alcalá":         ["Calle 127", "Calle 100"],
    "Niza":           ["Pepe Sierra", "Calle 100"],
    "Calle 100":      ["Alcalá", "Niza", "Virrey"],
    "Virrey":         ["Calle 100", "Centro"],
    "Centro":         ["Virrey", "Portal Sur"],
    "Portal Sur":     ["Centro"],
} #lista completa de estaciones y sus conexiones

def ruta_minima(grafo, origen, destino):
    if origen == destino:
        return [origen] #si estamos en el mismo nodo, la ruta es solo ese nodo

    visitados = set()
    cola = deque([[origen]])  # cola de rutas

    while cola:
        ruta = cola.popleft()
        nodo = ruta[-1]

        if nodo == destino:
            return ruta

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo.get(nodo, []):
                nueva_ruta = ruta + [vecino]
                cola.append(nueva_ruta)

    return None  # no hay camino


print(ruta_minima(metro, "Portal Norte", "Centro"))