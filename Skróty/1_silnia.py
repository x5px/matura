'''
Skrót przydatny na maturę
#1 - jednolinijkowa silnia
Jakub Rutkowski 2024
'''

def silnia(n):
    return n*silnia(n-1) if n>1 else 1

print(silnia(5)) # 120