import time

# def amigos(MAX):
#     t1=time.time()
#     for i in range(MAX):
#         s=0
#         for j in range (1,i-1+1):
#             if i%j==0:
#                 s+=j
#         s2=0
#         for k in range (1,s-1):
#             if s%k==0:
#                 s2+=k
#         if i==s2:
#             print(i,s)
#     t2=time.time()
#     print(t2-t1)


def amigos(MAX):
    amigos = set()
    prints = []
    t1=time.time()
    for i in range(MAX):
        if i not in amigos:
            posible_amigo = suma_de_divisores(i)
            if posible_amigo == i:
                prints.append((i,i))
                amigos.add(i)
            else:
                result = suma_de_divisores(posible_amigo)
                if result == i:
                    amigos.add(i)
                    amigos.add(posible_amigo)
                    prints.append((i,posible_amigo))
    t2=time.time()
    print(t2-t1)
    for p in prints:
        print(p)


def suma_de_divisores(n):
    if n <= 1:
        return 0
    
    # Iterar hasta sqrt(n)
    sum = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i != n:  
                sum += i
            if n // i != n:  
                sum += n//i
    
    
    return sum
    

def main():

    
    amigos(1000000)


if __name__ == "__main__":
    main()