import time
import matplotlib.pyplot as plt
from sieve import amigos

# Ranges to test
ranges = [50000, 100000, 150000, 200000, 250000]
times = []

for MAX in ranges:
    print(f"Testing MAX = {MAX}")
    elapsed = amigos(MAX)
    times.append(elapsed)


# Plotting
plt.plot(ranges, times, marker="o")
plt.xlabel("Valor MAX")
plt.ylabel("Tiempo de Ejecución (segundos)")
plt.title("Tiempo de ejecución de amigos() para diferentes rangos")
plt.xticks(ranges)
plt.grid(True)
plt.savefig("sieve_algorithm.png", dpi=300, bbox_inches="tight")
plt.show()
