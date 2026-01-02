numeros = []
numeros = input("Introduce una lista de números separados por comas: ").split(",")
Cantidad_numeros = len(numeros)

for i in range(Cantidad_numeros):
    for j in range(0, Cantidad_numeros - i - 1):
        if int(numeros[j]) > int(numeros[j + 1]):
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            print ("Cambio:", numeros[j], numeros[j + 1], "-", numeros[j + 1], numeros[j])
print ("Números ordenados de menor a mayor:", numeros)