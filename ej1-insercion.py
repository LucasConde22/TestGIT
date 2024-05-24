def ordenar(lista):
    for indice in range(len(lista)):
        insertar_ord(indice, lista)

def insertar_ord(indice, lista):
    actual = lista[indice]
    indice_j = indice - 1

    while indice_j > 0 and lista[indice_j] > actual:
        lista[indice_j + 1] = lista[indice_j]
        indice_j -= 1
    lista[indice_j + 1] = actual

l = [0, 9, 3, 8, 5, 3, 2, 4]
ordenar(l)
print(l)