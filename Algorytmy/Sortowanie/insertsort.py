
def insertsort(liczby):
    for i in range(1,len(liczby)):
        j = i
        while liczby[j] < liczby[j-1] and j > 0:
            liczby[j], liczby[j-1] = liczby[j-1], liczby[j]
            j -= 1
    return liczby

liczby = [7,3,9,4,10,5,2]
print(f"liczby przed sortowaniem: {liczby}")

liczby = insertsort(liczby)  
print(f"liczby po sortowaniu: {liczby}")