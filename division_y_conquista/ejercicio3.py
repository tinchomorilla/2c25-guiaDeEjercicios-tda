# (★) Implementar un algoritmo que, por división y conquista, permita obtener 
# la parte entera de la raíz cuadrada de 
# un número n, en tiempo O(logn). Por ejemplo, para n=10 debe devolver 3, 
# y para n=25 debe devolver 5. Justificar la complejidad del algoritmo.


def obtener_parte_entera(n):
    mid = n//2
    return obtener(n, mid)

def obtener(n, mid):
    if mid*mid > n:
        mid = mid//2
        return obtener(n,mid)

    if mid*mid <= n:
        if (mid+1)*(mid+1) <= n:
            mid = obtener(n, mid+1)
        return mid
    
def main():

    n = 10
    print(obtener_parte_entera(n)) # 3 
    
    n = 25
    print(obtener_parte_entera(n)) # 5

    n = 57
    print(obtener_parte_entera(n)) # 7

    n = 98
    print(obtener_parte_entera(n)) # 9


if __name__ == "__main__":
    main()