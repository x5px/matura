def loadfile(filename):
    with open(f'../../Dane_PR/{filename}.txt') as f:
        tab = [i.strip() for i in f.readlines()]
        return tab

def rozne_litery(tab):
    max_ct = 0
    max_ct_str = ''
    for i in tab:
        ct = 0
        txt = []
        for j in i:
            if j not in txt:
                txt.append(j)
        if len(txt) > max_ct:
            max_ct = len(txt)
            max_ct_str = i
    return max_ct_str + ' ' +  str(max_ct)

tab = loadfile('sygnaly')
print(rozne_litery(tab))


