"""
MATURA 2023
Jakub Rutkowski

#2 - Liczby pierwsze i sito Eratostenesa

Liczba pierwsza - liczba, która dzieli się jedynie przez 1 i samą siebie.
"""

import math

def sito(n):
    tab = [True] * (n+1)

    for i in range(2, math.ceil(n**0.5)):
        if tab[i] == True:
            for j in range(i*i, n+1, i):
                """
                Startuj od i*i (2 >>> 4)
                Przeskakuj co iloczyn (2, 4, 6, 8,...)
                aż do n+1 (bo Python liczby od 0)
                """
                tab[j] = False
    return tab[2:] # <-- pomijamy 0 i 1

tab = sito(15)

for k, v in enumerate(tab):
    print(k+2, v)