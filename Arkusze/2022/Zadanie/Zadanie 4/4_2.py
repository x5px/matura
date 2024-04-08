import math
'''
Zadanie 4.2

'''

def sito(n):
    pierwsze = []
    tab = [True] * (n+1)
    if n <= 1:
        return [None]
    for i in range(2, math.ceil(math.sqrt(n))): # 2-4
        if tab[i]:
            for j in range(i*i, n+1, i): # 1 - 4, 2
                tab[j] = False

    for i in range(2,n+1):
        if tab[i]:
            pierwsze.append(i)

    return pierwsze

# print(sito(210))

def czynniki_pierwsze_single(n):
    i_start = n
    l_czynnikow = sito(n)
    print(l_czynnikow)
    ind = 0
    czynniki = []
    while(n > 1):
        if(n%l_czynnikow[ind] != 0):
            ind += 1

        if n in l_czynnikow:
            czynniki.append(n)
            print("Break at " + str(n) + " index: " + str(ind), " no: " + str(l_czynnikow[ind]))
            break

        czynniki.append(l_czynnikow[ind])
        n_start = n
        n = n // l_czynnikow[ind]
        print(f"{n_start} // {l_czynnikow[ind]} == {n}")
    return (i_start, (czynniki, list(set(czynniki))))

def czynniki_pierwsze(filename):
    with open(f'../../Dane_2205/{filename}.txt', 'rt') as f:
        txt =  [int(i.replace('\n', '')) for i in f.readlines()]

    all_max = (0, 0)
    set_max = (0, 0)

    for i in txt:
        i_start = i
        l_czynnikow = sito(i)
        ind = 0
        czynniki = []
        while(i > 1):
            while (i%l_czynnikow[ind] != 0):
                ind += 1
            if i in l_czynnikow:
                czynniki.append(i)
                break

            czynniki.append(l_czynnikow[ind])
            i = i // l_czynnikow[ind]

        if len(czynniki) > all_max[1]:
            all_max = (i_start, len(czynniki))

        if len(list(set(czynniki))) > set_max[1] :
            set_max = (i_start, len(list(set(czynniki))))


    return (all_max, set_max)
#
#print(czynniki_pierwsze('przyklad'))
print(czynniki_pierwsze('liczby'))
# print(czynniki_pierwsze_single(20992))
# print(czynniki_pierwsze_single(99792))
# print(czynniki_pierwsze_single(420))
# print(czynniki_pierwsze_single(210))
# print(czynniki_pierwsze_single(62790))

# print(1891 % 7)