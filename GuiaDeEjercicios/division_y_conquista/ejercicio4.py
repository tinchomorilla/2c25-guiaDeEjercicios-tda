#(★) Se tiene un arreglo de N>=3 elementos en forma de pico, 
# esto es: estrictamente creciente hasta una determinada posición p, 
# y estrictamente decreciente a partir de ella (con 0<p<N-1). 
# Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] 
# la posición del pico es p=2. 
# Se pide: 
# a. Implementar un algoritmo de división y conquista de complejidad O(logn)
# que encuentre la posición p del pico. 
# b. Justificar la complejidad del algoritmo mediante el teorema maestro.

#[1,2,3,4,5,6,7,6,5,4,-2,-3,-4] -> posicion 6

def obtener_posicion_pico(arr):
    return obtener_pico(arr, 0, len(arr) -1)

def obtener_pico(arr, left, right):

    if left > right:
        return None

    mid = (left+right)//2

    if arr[mid-1] < arr[mid] > arr[mid+1]:
        return mid

    if arr[mid] < arr[mid+1]:
        return obtener_pico(arr, mid+1, right)
    else:
        return obtener_pico(arr, left, mid-1)




def main():

    arr = [1,2,3,4,5,6,7,8,5,4,-2,-3,-4] 
    print(obtener_posicion_pico(arr)) # 7

    arr = [1,2,3,4,5,6,7,6,5,4,-2,-3,-4] 
    print(obtener_posicion_pico(arr)) # 6

    arr = [1, 2, 3, 1, 0, -2] 
    print(obtener_posicion_pico(arr)) # 2

    arr = [1, 2, 1, 0, -1, -2] 
    print(obtener_posicion_pico(arr)) # 1

    arr = [3, 2, 1, 0, -1, -2] 
    print(obtener_posicion_pico(arr)) # 0

    arr = [1, 0, -1]
    print(obtener_posicion_pico(arr)) # 0
    

if __name__ == "__main__":
    main()