from collections import Counter

def countDopisane(tab):
    dopisane = []
    for txt in tab:
        a = txt.split()
        if a[0] == 'DOPISZ':
            dopisane.append(a[1])
    a = Counter(dopisane)
    for el in filter(lambda x: a[x] == max(a.values()), a): # filtr dla znajdowania elementu o najwyższej wartości w counterze a
        return ' '.join([el, str(max(a.values()))])

def countDopisaneNoCounter(tab):
    dopisane = {}
    for txt in tab:
        a = txt.split()
        if a[0] == 'DOPISZ':
            if a[1] not in dopisane.keys():
                dopisane[a[1]] = 1
            else:
                dopisane[a[1]] += 1
    for el in filter(lambda x: dopisane[x] == max(dopisane.values()), dopisane):
        print(' '.join([el, str(max(dopisane.values()))]))

def getDataFromFile(path):
    with open(f'../../DANE_2105/{path}.txt') as f:
        lines = f.readlines()
    tab = [i.strip() for i in lines]
    return tab

countDopisaneNoCounter(getDataFromFile('instrukcje'))

