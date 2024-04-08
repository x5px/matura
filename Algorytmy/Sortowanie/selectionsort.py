liczby = [2, 5, 1, 8, 4, 0, 9]

def selection_sort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i, len(lista)):
            if lista[min]> lista[j]:
                min = j
        lista[i], lista[min] = lista[min], lista[i]
    return lista

print(selection_sort(liczby))                