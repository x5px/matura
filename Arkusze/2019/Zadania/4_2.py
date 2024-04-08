def loadfile(filename):
    with open(f'../Dane_PR/{filename}.txt') as f:
        tab = []
        for l in f.readlines():
            l = int(l.replace('\n', ''))
            tab.append(l)
    return tab

def silnia(n):
    if n <= 1:
        return 1
    else:
        return n * silnia(n - 1)


def sprawdz_silnie(tab):
    for i in tab:
        i_str = str(i)
        suma_silni = sum([silnia(int(i)) for i in i_str])
        if suma_silni == i:
            print(i)

def sprawdz_silnie_1(i):
    i_str = str(i)
    suma = 0
    for j in i_str:
        print(f"{j}! = {silnia(int(j))}")
        suma += silnia(int(j))
        print(f"{suma} vs {i_str}")



# tab = loadfile('przyklad')
# sprawdz_silnie(tab)
#
# print('---------------')
tab = loadfile('liczby')
sprawdz_silnie(tab)

# sprawdz_silnie_1(40585)

