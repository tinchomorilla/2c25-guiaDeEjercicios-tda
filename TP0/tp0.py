import time


def amigos(MAX):
    cache = {}
    prints = [(0,0)]  # caso base 
    t1 = time.time()
    
    for i in range(2, MAX+1):  # arranco en 2 hasta MAX
        if i not in cache:
            cache[i] = suma_de_divisores(i)
            posible_amigo = cache[i]

            # caso numero perfecto
            if posible_amigo == i:
                prints.append((i, i))
                continue

            # chequeamos simetria
            if posible_amigo not in cache:
                cache[posible_amigo] = suma_de_divisores(posible_amigo)

            # condicion de amistad
            if (posible_amigo in cache and cache[posible_amigo] == i):
                prints.append((i, posible_amigo))

    t2 = time.time()
    log_prints(prints, t2 - t1)


def suma_de_divisores(n):
    # Iterar hasta sqrt(n)
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i != n:  
                sum += i
            if n // i != n:  
                sum += n//i
    return sum


def log_prints(prints, elapsed_time):
    for p in prints:
        print(p)
    print("Cantidad de pares amigos:", len(prints))
    print("El tiempo es de:", elapsed_time)
    

def main():

    amigos(1000000)

if __name__ == "__main__":
    main()