# (★★) Las bolsas de un supermercado se cobran por separado 
# y soportan hasta un peso máximo P, por encima del cual se rompen. 
# Implementar un algoritmo greedy que, teniendo una lista de pesos de 
# n productos comprados, encuentre la mejor forma de distribuir los productos 
# en la menor cantidad posible de bolsas. 
# Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 
# y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. 
# ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar. 
# Indicar y justificar la complejidad del algoritmo implementado.

####################################################################

# No es un algoritmo greedy OPTIMO, en el ejemplo del enunciado,
# este algoritmo devuelve 4 bolsas, cuando en realidad 
# lo optimo es que devuelva 3 bolsas.

####################################################################

def minimizar_cant_bolsas(arr_peso, w):
    arr = sorted(arr_peso, reverse=True)

    return minimizar(arr,w)

def minimizar(arr,w):

    cant_bolsas = 0
    sum = 0

    for i, peso in enumerate(arr):
        sum += peso
        if sum == w:
            cant_bolsas+=1
            sum = 0
        elif sum > w:
            cant_bolsas+=1
            sum = peso
        elif i == len(arr) - 1:
            cant_bolsas+=1

    return cant_bolsas

def main():

    arr_peso = [ 4, 2, 1, 3, 5 ]  # [5,4,3,2,1]
    w = 5
    print(minimizar_cant_bolsas(arr_peso, w)) # 4 bolsas

    arr_peso = [ 1, 1, 1, 1, 1 ]  # [1,1,1,1,1]
    w = 5
    print(minimizar_cant_bolsas(arr_peso, w)) # 1 bolsa

    arr_peso = [ 4, 2, 2, 3, 5 ]  # [5,4,3,2,2]
    w = 5
    print(minimizar_cant_bolsas(arr_peso, w)) # 4 bolsas

    arr_peso = [ 4, 1, 3, 5 ]  # [5,4,3,1]
    w = 5
    print(minimizar_cant_bolsas(arr_peso, w)) # 3 bolsas

    arr_peso = [ 4, 1, 3, 5 , 1]  # [5,4,3,1,1]
    w = 5
    print(minimizar_cant_bolsas(arr_peso, w)) # 3 bolsas

    arr_peso = [ 4, 1, 3, 1, 5 , 1]  # [5,4,3,1,1,1]
    w = 5
    print(minimizar_cant_bolsas(arr_peso, w)) # 4 bolsas



if __name__ == "__main__":
    main()