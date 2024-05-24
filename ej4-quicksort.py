def quicksort(lista):
    if len(lista) < 2:
        return lista
    menores, pivot, mayores = particionar(lista)
    return quicksort(menores) + [pivot] + quicksort(mayores)

def particionar(lista):
    pivot = lista[0]
    menores = []
    mayores = []

    for i in range(1, len(lista)):
        if lista[i] < pivot:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return menores, pivot, mayores

print(quicksort([6, 0, 3, 2, 5, 7, 4, 1]))