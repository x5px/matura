# Zadanie 3 Matura 2023

def fragmenty_2_cyfrowe(tab):
    frag = []
    for i in range(0, len(tab)-1):
        frag.append((tab[i], tab[i+1]))

    ct = 0
    for i in frag:
        print(i[0], i[1])
        if int(str(i[0]) + str(i[1])) > 90:
            ct += 1
    print(ct)

with open('../../Dane_2305/pi.txt') as f:
    liczby = [int(i.replace('\n','')) for i in f.readlines()]

fragmenty_2_cyfrowe(liczby)