'''
Jakub R
Matura 2017
Zadanie nr 6.4
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

print(loadfile('przyklad'))