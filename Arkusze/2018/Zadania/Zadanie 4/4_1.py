def loadfile(filename):
    with open(f'../../Dane_PR/{filename}.txt') as f:
        tab = [i.strip() for i in f.readlines()]
        return tab

tab = loadfile('sygnaly')

str = ''
for i in range(39, len(tab), 40):
    str += tab[i][9]

print(str)