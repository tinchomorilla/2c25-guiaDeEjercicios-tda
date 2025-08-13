# (★) Se tiene un sistema monetario (ejemplo, el nuestro).
# Se quiere dar “cambio” de una determinada cantidad de plata.
# Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes.
# El algoritmo recibirá un arreglo de valores del sistema monetario,
# y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben
# ser utilizados para minimizar la cantidad total utilizda.
# Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo implementado encuentra siempre la solución óptima?
# Justificar si es óptimo, o dar un contraejemplo. ¿Por qué se trata de un algoritmo Greedy? Justificar

# Ejemplo1: arr = [5,1,2,9,4] , 10 pesos.
# # sorted_arr = [9,5,4,2,1]
# En este caso podria ser,
# una solucion OPTIMA seria un billete de 9 y otro de 1, 9 + 1 = 10.
# Otra solucion NO optima seria: 5 + 4 + 1 = 10
# sorted_arr = [9,5,4,2,1]

# Ejemplo2: arr = [5,3,1,8,4], 10 pesos
# sorted_arr = [8,5,4,3,1]


def minimizar_cambio(arr, n): 
    return minimizar(arr, n)


def minimizar(arr, n):
    sist_monetario = sorted(arr, reverse=True)
    cambio = []
    sum = 0

    for i, billete_mayor in enumerate(sist_monetario):
        sum = billete_mayor
        cambio.append(billete_mayor)
        for billete_menor in sist_monetario[i + 1 :]:
            if no_me_pase(sum, billete_menor, n):
                sum = sum + billete_menor
                cambio.append(billete_menor)

            if sum == n:
                return cambio

        if sum == n:
            return cambio
        else:
            cambio = []
            sum = 0 

    return cambio


def no_me_pase(sum, nuevo, n):
    return sum + nuevo <= n



def main():

    arr = [5, 1, 2, 9, 4]
    n = 10
    print(minimizar_cambio(arr, n))  # [9,1]

    arr = [5, 1, 2, 44, 4]
    n = 10
    print(minimizar_cambio(arr, n))  # [5,4,1]

    arr = [5, 1, 2, 14, 4]
    n = 15
    print(minimizar_cambio(arr, n))  # [14,1]

    arr = [5, 1, 2, 11, 4]
    n = 15
    print(minimizar_cambio(arr, n))  # [11,4]

    arr = [5, 1, 2, 16, 4, 6]
    n = 15
    print(minimizar_cambio(arr, n))  # [6,5,4]


if __name__ == "__main__":
    main()
