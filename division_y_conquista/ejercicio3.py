# (★) Implementar un algoritmo que, por división y conquista, permita obtener 
# la parte entera de la raíz cuadrada de 
# un número n, en tiempo O(logn). Por ejemplo, para n=10 debe devolver 3, 
# y para n=25 debe devolver 5. Justificar la complejidad del algoritmo.


def obtener_parte_entera(n):
    return obtener(n, 1)

def obtener(n, x):

    if x*x > n:
        return x-1
    
    return obtener(n, x+1)

def main():

    n = 10
    print(obtener_parte_entera(n)) # 3 
    
    n = 25
    print(obtener_parte_entera(n)) # 5

    n = 57
    print(obtener_parte_entera(n)) # 7


if __name__ == "__main__":
    main()