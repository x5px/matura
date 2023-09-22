from dekoratory import pomiar_czasu
"""
MATURA 2024
Jakub Rutkowski

6 - Rekurencja: Ciąg Fibonacciego

Definicja:
Start - [0,1]
Każda kolejna liczba jest sumą dwóch poprzednich.
Czyli:
dla n = 0 >>> 0
dla n = 1 >>> 1
dla n > 1 >>> f(n-2)+f(n-1)
"""
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1) + fib(n-2)

@pomiar_czasu
def printall():
    for i in range(0, 50):
        print(fib(i))

printall()