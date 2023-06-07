# 1. Haciendo uso de comprensión de listas realice un programa que, dado una lista de listas de números enteros, devuelva el máximo de cada lista. Por ejemplo, suponga la siguiente listas de listas:
# [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
# El programa debe devolver el mayor elemento de cada sublista (señalado en negrita).
# Ahora, haciendo uso del pdb, inserte puntos de parada justo en la línea donde ha implementado la compresión de listas. Haga pruebas mostrando el contenido de las variables y continuar con la ejecución línea a línea. ¿Qué conclusiones obtiene?

# import pdb
# pdb.set_trace()

lista = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
for l in lista:
    mayor = max(l)
    print (mayor)

# 2. Haga uso de la función filter para construir un programa que, dado una lista de n números devuelva aquellos que son primos. Por ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente debe devolver como resultado [3, 5, 5, 13]

def primo(numero):
    if numero < 2:    # no son primos
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

lista = [3, 4, 8, 5, 5, 22, 13]
numeros_primos = list(filter(primo, lista))

print(numeros_primos)
