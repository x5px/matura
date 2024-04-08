def makeNapis(tab):
    napis = []
    for txt in tab:
        a = txt.split()
        if a[0] == 'DOPISZ':
            napis.append(a[1])
        elif a[0] == 'USUN':
            napis.pop()
        elif a[0] == 'ZMIEN':
            napis[-1] = a[1]
        elif a[0] == 'PRZESUN':
            try:
                ind = napis.index(a[1])
            except ValueError:
                pass
            if a[1] == 'Z':
                napis[ind] = 'A'
            else:
                napis[ind] = chr(ord(napis[ind]) + 1)
    return ''.join(napis)

def getDataFromFile(path):
    with open(f'../../DANE_2105/{path}.txt') as f:
        lines = f.readlines()
    tab = [i.strip() for i in lines]
    return tab

#print(makeNapis(getDataFromFile('przyklad')))
# >>> ALANTURING

print(makeNapis(getDataFromFile('instrukcje')))

