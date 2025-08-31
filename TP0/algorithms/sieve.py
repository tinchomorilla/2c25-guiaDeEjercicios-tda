import time

def sieve_divisores(MAX):
    # S[n] = sum of proper divisors of n
    S = [0] * (MAX + 1)
    for d in range(1, MAX // 2 + 1):
        for m in range(2 * d, MAX + 1, d):
            S[m] += d
    return S

def amigos(MAX):
    t1 = time.time()
    S = sieve_divisores(MAX)

    # include (0,0) as a special case
    prints = [(0, 0)]

    for i in range(2, MAX + 1):
        s = S[i]
        # Case 1: Perfect number (sum of divisors == itself)
        if s == i:
            prints.append((i, i))
        # Case 2: Amicable numbers (avoid duplicates, i < s)
        elif s > i and s <= MAX and S[s] == i:
            prints.append((i, s))

    t2 = time.time()
    log_prints(prints, t2 - t1)
    return t2 - t1

def log_prints(prints, elapsed_time):
    for p in prints:
        print(p)
    print("Cantidad de pares amigos:", len(prints))
    print("El tiempo es de:", elapsed_time)
