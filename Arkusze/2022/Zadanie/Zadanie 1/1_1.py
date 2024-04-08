import copy

def b_sort(tab):
    for i in range(len(tab)-1):
        for j in range(0, len(tab)-1-i):
            if(tab[j] > tab[j+1]):
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

def znajdz_brakujace(tab):
    tab2 = copy.deepcopy(tab)
    brak = []
    if tab[0] != 1:
        brak = [j for j in range(1, tab[0])]

    for i in brak:
        tab2.append(i)

    tab2 = b_sort(tab2)
    #print(tab2)

    for i in range(1, len(tab2)+1):
        if(i not in tab2):
            brak.append(i)

    # tab = b_sort(tab)
    # print(tab)

    return brak

def permutacja(tab):
    tab = b_sort(tab)
    brak = znajdz_brakujace(tab)
    count = len(brak)

    for i in range(1, len(tab)-1):
        for j in range(1, len(tab)):
            if(tab[i] == j):
                count += 1
                break
    if len(brak) == 0:
        return 0
    return int(count/2)

print(permutacja([1, 3, 1]))
print(permutacja([1, 4, 2, 5]))
print(permutacja([2, 2, 2, 2, 2]))
print(permutacja([4, 2, 3, 1]))
print(permutacja([5, 4, 1, 5, 6, 8]))
print(permutacja([8, 4, 9, 6, 5, 7]))
