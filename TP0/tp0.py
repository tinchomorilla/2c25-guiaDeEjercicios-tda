import time


def amigos(MAX):
    t1 = time.time()
    cache = {i: suma_de_divisores(i) for i in range(2, MAX+1)}
    prints = [(0,0)]
    for i in range(2, MAX+1):
        posible_amigo = cache[i]
        if posible_amigo == i:
            prints.append((i, i))
            continue
        if cache.get(posible_amigo, 0) == i:
            if i < posible_amigo:  # evitar duplicados
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

    amigos(250)

if __name__ == "__main__":
    main()