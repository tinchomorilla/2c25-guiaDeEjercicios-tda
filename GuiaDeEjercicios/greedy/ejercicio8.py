# (★★) Tenemos una mochila con una capacidad W. Hay elementos a guardar,
# cada uno tiene un valor, y un peso que ocupa de la capacidad total.
# Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.
# Implementar un algoritmo Greedy que, reciba dos arreglos de valores y pesos de los elementos,
# y devuelva qué elementos deben ser guardados para maximizar la ganancia total.
# Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
# ¿Por qué se trata de un algoritmo Greedy? Justificar
# ¿Qué diferencias se perciben si en vez de tener que colocar los elementos completos, 
# se pueden fraccionar para nuestra conveniencia?

#########################################################################################################

# Ejemplo donde mi algoritmo no es optimo:
# Capacidad W = 8

# Pesos = [3, 4, 5]
# Valores = [60, 100, 120]

# Ratio valor/peso = [20, 25, 24]

# 1- Greedy toma primero el ítem con ratio más alto → el de peso 4 y valor 100.
# Capacidad restante = 4.

# 2- El siguiente ratio más alto es el de peso 5 (no entra), así que toma el de peso 3 y valor 60.
# Capacidad usada = 7. Valor total = 160.

# 💡 Óptimo real 0/1:
# Tomar ítems de peso 3 y 5 (valores 60 + 120) → peso 8, valor 180 ✅ → más que 160.

# Mi algoritmo hubiese elegido los valores [4,3] en vez de [5,3]

#########################################################################################################

PESO = 1
RATIO = 0


def obtener_ratio(arr_valor, arr_peso):
    arr = []
    for i in range(len(arr_peso)):
        ratio = arr_valor[i] / arr_peso[i]
        tuple = (ratio, arr_peso[i])
        arr.append(tuple)

    return arr


def maximizar_valor(arr_valor, arr_peso, w):
    arr = obtener_ratio(arr_valor, arr_peso)
    arr = sorted(arr, key=lambda x: x[RATIO], reverse=True)

    return maximizar(arr, w)


def maximizar(arr, w):
    elementos = []
    sum = 0
    for ratio, peso in arr:

        if len(elementos) == 0 or no_me_pase(sum, peso, w):
            sum = sum + peso
            elementos.append(peso)

        if sum == w:
            return elementos

    return elementos


def no_me_pase(peso_hasta_el_momento, peso_a_agregar, w):
    return peso_hasta_el_momento + peso_a_agregar <= w


def main():

    arr_peso = [5, 1, 2, 4]
    arr_valor = [10, 100, 50, 50]
    w = 10
    # [(100.0, 1), (25.0, 2), (12.5, 4), (2.0, 5)] --> [(ratio, peso)]

    print(maximizar_valor(arr_valor, arr_peso, w))  # [1,2,4]


if __name__ == "__main__":
    main()

