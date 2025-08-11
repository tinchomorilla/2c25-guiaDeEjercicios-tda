# (★★) Dada un aula/sala donde se pueden dar charlas. 
# Las charlas tienen horario de inicio y fin. 
# Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, 
# representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin, 
# e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas. 
# Cada charla vale lo mismo, es decir, da lo mismo que charla doy. Es irrelevante la duracion de la charla.
# Es decir si doy una charla de una hora o una charla de 10 horas, es lo mismo. Ahora, si doy 2 charlas de 1 hora
# y una charla de 10 horas, prefiero las 2 charlas de una hora. Si puedo dar las 3 doy las 3,
# pero si no priorizo maximizar.
# No se pueden dar charlas al mismo tiempo. No se pueden solapar.
# Indicar y justificar la complejidad del algoritmo implementado.

# Ejemplo1:
# arr= [(1,2) , (2,8), (7,8), (5,8), (3,5), (1,10), (1,4)]
# sorted_arr= [(1,2) , (1,4), (3,5), (2,8), (7,8), (5,8) , (1,10)] # ORDENADO POR HORARIO FIN
# Result = [(1,2), (3,5), (7,8)]


# Ejemplo2:
# arr= [(2,4), (7,8), (4,5), (5,8), (3,5), (1,10), (1,4), (2,5), (3,9)]
# sorted_arr= [(2,4) , (1,4), (3,5), (4,5), (2,5), (5,8), (7,8), (3,9), (1,10)] # ORDENADO POR HORARIO FIN
# Result = [(2,4), (4,5), (5,8)]


# Justificacion de la complejidad:
# La funcion -> sorted(arr, key=lambda x: x[FIN])
# usa Timsort en Python, que es O(n log n) en el caso promedio y peor caso.
# Este es el paso que domina la complejidad final.
# El recorrido: "for horario in horarios_ordenados:"
# hace a lo sumo n iteraciones, y cada chequeo (se_solapan) es O(1).
# Por lo tanto, esta parte es O(n).
# Complejidad total = T(n)=O(nlogn)+O(n)=O(nlogn)


##############################################################################################


FIN = 1
INICIO = 0

def maximizar_charlas(arr):
    # Ordenar por fin
    sorted_arr = sorted(arr, key=lambda x: x[FIN])
    return maximizar(sorted_arr)

def se_solapan(anterior, nueva):
    return anterior[FIN] > nueva[INICIO]

def maximizar(horarios_ordenados):
    charlas = []
    for horario in horarios_ordenados:
        if len(charlas) == 0 or not se_solapan(charlas[-1], horario):
            charlas.append(horario)
    return charlas

def main():
    
    # Se esta maximizando la cantidad de charlas en el aula
    # pero sin pensar "en el futuro", es decir, se agarra la primer charla
    # pero sin fijarse si la siguiente dentro de su horario FIN es mas corta o no.
    # Ya que si se agarrase la mas corta (dentro de su mismo horario FIN), 
    # en un futuro podrian agregarse charlas mas cortas entre medio de las que ya hay,
    # dejando huecos para mas charlas (sin que se solapen por supuesto)

    # Ejemplo1
    arr = [(1,2), (2,8), (7,8), (5,8), (3,5), (1,10), (1,4)]
    print(maximizar_charlas(arr))  # [(1,2), (3,5), (7,8)]

    # Ejemplo2
    arr = [(2,4), (4,5), (5,8), (3,5), (1,10), (1,4), (2,5), (3,9), (7,8)]
    print(maximizar_charlas(arr))  # [(2,4), (4,5), (5,8)]

    # Ejemplo3
    arr = [(2,4), (7,8), (4,5), (5,8), (3,5), (1,10), (1,4), (2,5), (3,9)] 
    print(maximizar_charlas(arr))  # [(2,4), (4,5), (7,8)]

    # El ejemplo2 y ejemplo3 tienen el mismo arreglo pero en != orden, lo logico seria que
    # de ese mismo arreglo del ejemplo2, nos de la solucion del ejemplo3.
    # De esta forma, en un futuro podriamos agregar 2 charlas como por ejemplo con
    # los horarios (5,6) y (6,7). Pero en el ejemplo2, ya no seria posible, 
    # porque se solaparian con la charla (5,8). 
    # Igualmente es solo un comentario mio, la resolucion cumple con lo que pide el enunciado.


if __name__ == "__main__":
    main()
