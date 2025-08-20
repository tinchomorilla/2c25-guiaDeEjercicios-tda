# (★★) Implementar un algoritmo que reciba un grafo y un número n que,
# utilizando backtracking, indique si es posible pintar cada vértice
# con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.


def colorear(grafo, n):
    vertices = grafo.obtener_vertices()
    colores = set(range(1, n + 1))
    v_pintados = {}  # mapeo vertice -> color
    return backtracking(grafo, v_pintados, vertices, 0, colores)


def backtracking(grafo, v_pintados, vertices, v_actual, colores):
    # Caso base: todos los vértices coloreados
    if v_actual >= len(vertices):
        return True

    # Obtener colores disponibles para el vértice actual
    colores_disponibles = obtener_colores_disponibles(
        grafo, v_pintados, vertices[v_actual], colores
    )

    # Probar cada color disponible
    for color in colores_disponibles:
        v_pintados[vertices[v_actual]] = color

        # Recursivamente intentar colorear los vertices restantes
        if backtracking(grafo, v_pintados, vertices, v_actual + 1, colores):
            return True

        # Backtrack: remover esta asignacion de color
        del v_pintados[vertices[v_actual]]

    # No se encontro un coloreo valido
    return False


def obtener_colores_disponibles(grafo, v_pintados, vertice_actual, colores):
    """Obtener colores que pueden ser usados para el vértice actual"""
    colores_usados = set()

    # Verificar colores de vertices adyacentes
    for vertice, color in v_pintados.items():
        if grafo.estan_unidos(vertice, vertice_actual):
            colores_usados.add(color)

    # Retornar colores disponibles
    return colores - colores_usados
