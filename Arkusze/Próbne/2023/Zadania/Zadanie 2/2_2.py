'''
Jakub R
Matura 2023 Próbna CKE
Zadanie nr 2.2
'''

def loadfile(filename):
    with open(f'../../DANE/DANE_M/{filename}.txt') as f:
        t = [i.strip() for i in f.readlines()]
        t[0] = int(t[0])
        t[2] = [int(i) for i in t[2].split(' ')]

    return t


def czy_mniejszy(n, s, k1, k2):
    # print(n, s, k1, k2)
    i = k1-1
    j = k2-1
    while ( i <= n-1 and j <= n-1 ):
        if(s[i] == s[j]):
            i = i + 1
            j = j + 1
        else:
            if (s[i] < s[j]):
                return "TAK"
            else:
                return "NIE"
    if( j <= n ):
        return "TAK"
    else:
        return "NIE"

det = loadfile('sufiks_1')
print(czy_mniejszy(det[0], det[1], det[2][0], det[2][1]))

det = loadfile('sufiks_2')
# print(det)
print(czy_mniejszy(det[0], det[1], det[2][0], det[2][1]))
