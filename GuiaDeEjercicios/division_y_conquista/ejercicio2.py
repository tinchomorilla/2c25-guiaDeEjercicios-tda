#(★) Se tiene un arreglo en el que se registran los resultados de tests automáticos de una porción de código. 
# Este código se encontraba funcionando pero, debido a unos cambios que se están realizando, 
# en algún momento dejó de funcionar. Se registra un 1 si pasa los tests, 0 en caso contrario. 
# De esta manera, el arreglo tendrá la forma [1, 1, 1, ..., 0, 0, ...] (es decir, unos seguidos de ceros). 
# Se pide: 
# a. una función de orden O(logn) que, por división y conquista, encuentre el índice del primer 0, 
# de forma que se pueda reconocer rápidamente en qué modificación del código se dejó de pasar los tests. 
# Si no hay ningún 0 (solo hay unos), debe devolver -1. 
# b. demostrar con el Teorema Maestro que la función es, en efecto, O(logn)
# Ejemplos:
# [1, 1, 1, 0, 0, 0 , 0 ,0] →  3
# [1, 1, 1, 1, 0, 0 , 0 ,0] →  4
# [1, 1, 1, 1, 1, 0 , 0 ,0] →  5
# [0, 0, 0, 0, 0] →  0
# [1, 1, 1, 1, 1] → -1
# [1, 0, 0, 0, 0] → 1



def buscar_primer_cero(arr):
    return buscar(arr, 0, len(arr) -1)

def buscar(arr, inicio, fin):
    if inicio > fin:
        return -1
    
    medio = (inicio + fin) // 2

    if arr[medio] == 0:
        # Estoy en el indice 0
        if medio == 0:
            return medio     
        # Encontre el primer 0    
        elif arr[medio-1] == 1:
            return medio
        else:
            # Voy hacia la izquierda quedandome con la mitad del arreglo
            return buscar(arr, inicio, medio)

    
    if arr[medio-1] == 1:
        # Voy hacia la derecha quedandome con la mitad del arreglo
        return buscar(arr, medio+1, fin)
    
         
    
        
def main():
    arr = [1, 1, 1, 0, 0, 0] 
    print(buscar_primer_cero(arr)) # 3

    arr = [1, 1, 1, 1, 1, 0 , 0 ,0] 
    print(buscar_primer_cero(arr)) # 5

    arr = [1, 0, 0, 0, 0] 
    print(buscar_primer_cero(arr)) # 1

    arr = [1, 1, 1, 1, 1]
    print(buscar_primer_cero(arr)) # -1

    arr = arr = [1, 1, 1, 1, 1, 1,0] 
    print(buscar_primer_cero(arr)) # 6

    arr = arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,0] #12
    print(buscar_primer_cero(arr)) # 6

    arr = [0, 0, 0, 0, 0] 
    print(buscar_primer_cero(arr)) # 0

    arr = [0, 0, 0] 
    print(buscar_primer_cero(arr)) # 0




if __name__ == "__main__":
    main()