'''
Cheapsort
K>K> 2023
'''

def cheapsort(liczby):
    n = len(liczby)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if liczby[j] < liczby[min_idx]:
                min_idx = j

        liczby[i], liczby[min_idx] = liczby[min_idx], liczby[i]

    return liczby


liczby = [64, 25, 12, 22, 11]
print("Liczby przed sortowaniem:", liczby)
sorted_liczby = cheapsort(liczby)
print("Posortowane liczby:", sorted_liczby)
