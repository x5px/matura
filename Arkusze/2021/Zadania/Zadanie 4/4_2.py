def znajdzNajdluzszyCiag(tab):
    counter = 0
    old_counter = 0
    instrukcja = ''
    for i in range(1, len(tab)):
        #print(f"{tab[i-1].split(' ')[0]} vs {tab[i].split(' ')[0]} ")
        if tab[i-1].split(' ')[0] == tab[i].split(' ')[0]:
            counter += 1
        else:
            if counter > old_counter:
                old_counter = counter
                instrukcja = tab[i-1].split(' ')[0]
            counter = 0
    return instrukcja + " " + str(old_counter+1)
def getDataFromFile(path):
    with open(f'../../DANE_2105/{path}.txt') as f:
        lines = f.readlines()
    tab = [i.strip() for i in lines]
    return tab

#print(znajdzNajdluzszyCiag(getDataFromFile('przyklad')))
# >>> DOPISZ 5
print(znajdzNajdluzszyCiag(getDataFromFile('instrukcje')))
