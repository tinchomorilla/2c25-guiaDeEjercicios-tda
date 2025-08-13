# (★) Se tiene un sistema monetario (ejemplo, el nuestro).
# Se quiere dar “cambio” de una determinada cantidad de plata.
# Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes.
# El algoritmo recibirá un arreglo de valores del sistema monetario,
# y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben
# ser utilizados para minimizar la cantidad total utilizda.
# Indicar y justificar la complejidad del algoritmo implementado.
# ¿El algoritmo implementado encuentra siempre la solución óptima?
# Justificar si es óptimo, o dar un contraejemplo. ¿Por qué se trata de un algoritmo Greedy? Justificar

# Ejemplo1: arr = [5,1,2,50,20] , 10 pesos.
# # sorted_arr = [50,20,5,2,1]
# En este caso podria ser,
# una solucion OPTIMA seria un billete de 9 y otro de 1, 9 + 1 = 10.
# Otra solucion NO optima seria: 5 + 4 + 1 = 10
# sorted_arr = [9,5,4,2,1]

# Ejemplo2: arr = [5,3,1,8,4], 10 pesos
# sorted_arr = [8,5,4,3,1]


def cambio_greedy(denoms, monto):

    denoms = sorted(denoms, reverse=True)
    restante = monto
    resultado = []

    for billete in denoms:
        if billete <= 0:   # por robustez
            continue
        usar = restante // billete
        if usar > 0:
            resultado.extend([billete] * usar)   
            restante -= usar * billete
        if restante == 0: 
            break

    # si no se pudo dar cambio exacto, avisamos 
    return resultado if restante == 0 else None




def main():

    arr = [5, 1, 2, 50]
    n = 10
    print(cambio_greedy(arr, n))  # [5,5]

    arr = [5, 1, 2, 20]
    n = 10
    print(cambio_greedy(arr, n))  # [5,5]

    arr = [5, 1, 2, 10]
    n = 15
    print(cambio_greedy(arr, n))  # [10,5]

    arr = [5, 1, 2, 50]
    n = 15
    print(cambio_greedy(arr, n))  # [5,5,5]

    arr = [1, 2, 10, 100, 50]
    n = 15
    print(cambio_greedy(arr, n))  # [10,2,2,1]

    arr = [5, 1, 2, 100, 10]
    n = 20
    print(cambio_greedy(arr, n))  # [10,10]


if __name__ == "__main__":
    main()
