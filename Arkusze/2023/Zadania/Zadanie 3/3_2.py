# Zadanie 3.2 Matura 2023

def find_min_max(tab):
    frag = []
    for i in range(0, len(tab)-1):
        frag.append(str(tab[i]) + str(tab[i+1]))

    print(frag)

    instances = {(str(i) + str(j)): 0 for i in range(0, 10) for j in range(0, 10)}
    print(instances)

    for i in frag:
        if i in instances.keys():
            instances[i] += 1

    maxval = max(instances.values())
    minval = min(instances.values())
    max_key = 0
    min_key = 0

    for i in instances.keys():
        if instances[i] == minval:
            min_key = i
            break

    for i in instances.keys():
        if instances[i] == maxval:
            max_key = i
            break

    print(str(min_key[0]) + str(min_key[1]), minval)
    print(str(max_key[0]) + str(max_key[1]), maxval)

with open('../../Dane_2305/pi.txt') as f:
    liczby = [int(i.replace('\n','')) for i in f.readlines()]

find_min_max(liczby)