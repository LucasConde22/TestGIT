def mergesort(lista):
    if len(lista) < 2:
        return lista
    izq = mergesort(lista[:len(lista)//2])
    der = mergesort(lista[len(lista)//2:])
    return merge(izq, der)

def merge(izq, der):
    i, j = 0, 0
    lista_final = []

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            lista_final.append(izq[i])
            i += 1
        else:
            lista_final.append(der[j])
            j += 1
    lista_final += izq[i:]
    lista_final += der[j:]
    return lista_final

print(mergesort([6, 0, 3, 2, 5, 7, 4, 1]))
