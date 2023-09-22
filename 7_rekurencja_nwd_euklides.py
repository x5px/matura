from dekoratory import pomiar_czasu
"""
MATURA 2024
Jakub Rutkowski

#7 - Rekurencja: Algorytm Euklidesa

Definicja:
Tak jak opisane w #5 - Rozkład na czynniki pierwsze, ale z użyciem rekurencji.
"""

def nwd(a, b):
    return nwd(b, a%b) if b else a # szybki sposób (if b >>> if b>0)
# zapamiętać!

def nwd_slow(a, b):
    if b>a:
        return nwd(b, a%b)
    return a

@pomiar_czasu
def nwd_iter(a, b): # metoda iteracyjna
    while b:
        a, b = b, a%b
    return a

"""
Wyjaśnienie:
282:78=3, reszty 48
78:48=1, reszty 30

"""

@pomiar_czasu
def solve_nwd():
    print(nwd(84, 126))
@pomiar_czasu
def solve_nwd_slow():
    print(nwd_slow(84, 126))

solve_nwd()
solve_nwd_slow()
print(nwd_iter(84, 126))
