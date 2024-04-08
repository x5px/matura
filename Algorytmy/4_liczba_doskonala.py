from dekoratory import pomiar_czasu
"""
MATURA 2024
Jakub Rutkowski

#4 - Liczba doskonała
(+#5 - Rozkład na czynniki pierwsze)

Liczba doskonała - liczba, której dzielniki równe są samej sobie.
Np. 6 = 1+2+3
"""
def czynniki_pierwsze(n):
    if n==1:
        return [1]
    tab = []
    for i in range(1, n):
        if n%i==0:
            tab.append(i)
    return tab

@pomiar_czasu
def czy_doskonala(n):
    print(n, "= ", end='')
    for i in czynniki_pierwsze(n):
        print(i, end=' + ')
    print()
    return n == sum(czynniki_pierwsze(n))

print(czy_doskonala(1)) # True
print(czy_doskonala(5)) # False
print(czy_doskonala(6)) # True
print(czy_doskonala(10)) # False
print(czy_doskonala(496)) # True
print(czy_doskonala(8128)) # True
