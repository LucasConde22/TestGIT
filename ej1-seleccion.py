def ordenar(lista):
    for indice in range(len(lista) - 1):
        minimo = buscar_minimo(lista, indice)
        lista[indice], lista[minimo] = lista[minimo], lista[indice]

def buscar_minimo(lista, indice):
    min = lista[indice]
    min_indice = indice
    for i in range(indice + 1, len(lista)):
        if lista[i] < min:
            min_indice = i
            min = lista[i]
    return min_indice

l = [0, 9, 3, 8, 5, 3, 2, 4]
ordenar(l)
print(l)