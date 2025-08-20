# (★★) Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero
# n menor a "V", devuelva si es posible obtener un subconjunto de n vertices tal que
# ningun par de vertices sea adyacente entre si.


def no_adyacentes(grafo, n):
    "Devolver una lista con los n vértices, o None de no ser posible"
    candidatos = set()
    vertices = grafo.obtener_vertices()
    resultado = backtracking(grafo, n, candidatos, vertices, 0)
    return list(resultado) if resultado is not None else None


def backtracking(grafo, n, candidatos, vertices, v_actual):
    if len(candidatos) == n:
        return candidatos

    if v_actual >= len(vertices):
        return None

    if es_compatible(grafo, candidatos, vertices[v_actual]):
        candidatos.add(vertices[v_actual])
        solucion = backtracking(grafo, n, candidatos, vertices, v_actual + 1)
        if solucion is not None:
            return solucion
        candidatos.remove(vertices[v_actual])

    return backtracking(grafo, n, candidatos, vertices, v_actual + 1)


def es_compatible(grafo, candidatos, nuevo_vertice):
    for v in candidatos:
        if grafo.estan_unidos(v, nuevo_vertice):
            return False
    return True
