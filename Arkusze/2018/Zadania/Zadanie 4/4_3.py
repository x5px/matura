def loadfile(filename):
    with open(f'../../Dane_PR/{filename}.txt') as f:
        tab = [i.strip() for i in f.readlines()]
        return tab

def w_len(w1, w2):
    return abs(int(ord(w1))-int(ord(w2)))

def dlugosc_liter(tab):
    ans = []
    for txt in tab:
        temp = ''
        for i in range(0, len(txt)):
            for j in range(0, len(txt)):
                if w_len(txt[i], txt[j]) > 10:
                    temp += txt[i] # xD
        #print(temp)
        if len(temp) == 0:
            ans.append(txt)
    return ans

# print(dlugosc_liter(['CGECF', 'ABEZA']))

tab = loadfile('sygnaly')
odp = dlugosc_liter(tab)

for i in odp:
    print(i)