'''
Jakub R
Matura 2017
Zadanie nr 6.1
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

def find_max_min(tab):
    bigtab = []
    for i in range(0, len(tab)):
        bigtab.extend(tab[i])

    return (max(bigtab), min(bigtab))

tab = loadfile('przyklad')
d_tab = loadfile('dane')

print(find_max_min(d_tab))