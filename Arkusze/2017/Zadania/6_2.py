'''
Jakub R
Matura 2017
Zadanie nr 6.2
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
def symetria(tab):
    ct = 0
    sr = len(tab[0])//2
    for i in range(0, len(tab)):
        #print(tab[i][:sr], " vs ", tab[i][sr:])
        if tab[i][:sr] != tab[i][sr:][::-1]:
            ct += 1
    return ct

tab = loadfile('przyklad')
d_tab = loadfile('dane')

print(symetria(d_tab))

