"""
MATURA 2024
Jakub Rutkowski

#8 - Wydawanie reszty metodą zachłanną

Definicja:
R - reszta
N - lista banknotów w obiegu [500, 200, 100, 50, 20, 10, 5, 2, 1]
Jeśli R < 0, zakończ.
Jeśli nie:
    Jeśli R < N[i] >>> i = i+1, zacznij od nowa
    Jeśli R > N[i]:
        L = R // N[i]
        R -= (N[i]* L)
        i = i+1

Źródło: http://www.algorytm.org/inne/problem-wydawania-reszty.html
"""


