''' 
Sortowanie bąbelkowe
K>K> 2023
'''

def buble_sort(liczby):
    for i in range(len(liczby)):
        for j in range(len(liczby)-1):
            if liczby[j] > liczby[j+1]:
                liczby[j], liczby[j+1] = liczby[j+1], liczby[j]
    print(f"Po sortowaniu: {liczby}")


liczby = [3, 6, 1, 2, 7, 9]
print(f"Przed: {liczby}")
buble_sort(liczby)
