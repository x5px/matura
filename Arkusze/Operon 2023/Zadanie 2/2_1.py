import math

def sito(pocz, konc):
    tab = [True] * konc
    max_l = math.ceil(math.sqrt(konc))
    for i in range(pocz, max_l):
        if i < 2:
            tab[i] = False
        else:
            for j in range(i*i, konc+1, i):
                tab[j] = False
    return tab

def getChain(tab):
    chain_tab = []
    counter = 0
    for i in range(len(tab)):
        if tab[i] == False:
            counter += 1
        else:
            counter = 0
        chain_tab.append(counter)
    return chain_tab

primes = sito(0, 31)
print(getChain(primes))