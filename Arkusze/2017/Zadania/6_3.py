'''
Jakub R
Matura 2017
Zadanie nr 6.3
'''

def loadfile(filename):
    with open(f"../Dane_PR/{filename}.txt") as f:
        tab = []
        for i in f.readlines():
            i = i.split(' ')
            for j in range(0, len(i)):
                i[j] = int(i[j])
            tab.append(i)

    return tab

def kontrastujace(tab):
    res = []
    for i in range(0, len(tab)-1):
        for j in range(0, len(tab[i])):
            if abs(int(tab[i+1][j] - int(tab[i][j]))) > 128:
                if (i, j) not in res:
                    res.append((i, j))
                if (i+1, j) not in res:
                    res.append((i+1, j))

    for i in range(0, len(tab)):
        for j in range(0, len(tab[i])-1):
            if abs(int(tab[i][j+1] - int(tab[i][j]))) > 128:
                if (i, j) not in res:
                    res.append((i, j))
                if (i, j+1) not in res:
                    res.append((i, j+1))

    return len(res)

tab = loadfile('przyklad')
d_tab = loadfile('dane')

# print(kontrastujace(tab))
print(kontrastujace(d_tab))
