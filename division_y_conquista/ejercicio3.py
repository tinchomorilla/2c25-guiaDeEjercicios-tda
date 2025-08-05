# (★) Implementar un algoritmo que, por división y conquista, permita obtener 
# la parte entera de la raíz cuadrada de 
# un número n, en tiempo O(logn). Por ejemplo, para n=10 debe devolver 3, 
# y para n=25 debe devolver 5. Justificar la complejidad del algoritmo.


def obtener_parte_entera(n):
    return buscar_raiz(n, 0, n)

def buscar_raiz(n, low, high):
    if low > high:
        return high  # el mayor número tal que mid^2 <= n

    mid = (low + high) // 2
    cuadrado = mid * mid

    if cuadrado == n:
        return mid
    elif cuadrado < n:
        return buscar_raiz(n, mid + 1, high)
    else:
        return buscar_raiz(n, low, mid - 1)
    
def main():

    n = 10
    print(obtener_parte_entera(n)) # 3 
    
    n = 25
    print(obtener_parte_entera(n)) # 5

    n = 57
    print(obtener_parte_entera(n)) # 7

    n = 98
    print(obtener_parte_entera(n)) # 9

    n = 99999
    print(obtener_parte_entera(n)) # 316


if __name__ == "__main__":
    main()