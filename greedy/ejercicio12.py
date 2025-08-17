# (★★) Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia
# y poder en la zona costera de Ciudad República.
# Allí reina el caos y la delincuencia, a tal punto que quien termina organizando
# las pequeñas mafias locales no es otro sino Arnook.
# En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos
# grupos por el control de diferentes kilómetros de la ruta costera.
# Cada pequeña mafia le pide a Arnook control sobre un rango de kilómetros
# (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ).
# Si hay una mafia tomando control de algún determinado kilómetro,
# no puede haber otra haciendo lo mismo (es decir, no pueden solaparse).
# Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”,
# indistintamente de los kilómetros pedidos.
# Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie,
# así que lo único que es de interés es maximizar la cantidad de permisos otorgados
# (asegurándose de no otorgarle algún lugar a dos mafias diferentes).
# Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia,
# y determine a cuáles se les otorgará control, de forma que no hayan dos mafias
# ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados.
# Indicar y justificar la complejidad del algoritmo implementado.
# Justificar por qué el algoritmo planteado es Greedy.
# ¿El algoritmo da la solución óptima siempre?


######################################################################

LIMITE_INFERIOR = 0
LIMITE_SUPERIOR = 1


def maximizar_permisos_otorgados(arr):
    arr = sorted(arr, key=lambda x: x[LIMITE_SUPERIOR])
    return maximizar(arr)


def maximizar(arr):
    rangos_otorgados = []
    for rango in arr:
        if len(rangos_otorgados) == 0 or no_se_solapa(rangos_otorgados[-1], rango):
            rangos_otorgados.append(rango)

    return rangos_otorgados


def no_se_solapa(rango_anterior, rango_nuevo):
    return rango_nuevo[LIMITE_INFERIOR] >= rango_anterior[LIMITE_SUPERIOR]


def main():

    # [ (1,3), (3,4), (2,5), (5,7), (12,14), (8,15), (14,15)] -> sorted array
    arr_rangos = [(8, 15), (3, 4), (12, 14), (2, 5), (1, 3), (5, 7), (14, 15)]
    print(
        maximizar_permisos_otorgados(arr_rangos)
    )  # [(1, 3), (3, 4), (5, 7), (12, 14), (14, 15)] -> 5 permisos


if __name__ == "__main__":
    main()
