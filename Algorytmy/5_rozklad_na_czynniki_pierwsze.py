"""
MATURA 2024
Jakub Rutkowski

5 - Rozkład na czynniki pierwsze
"""
def czynniki_pierwsze(n):
    if n==1:
        return [1]
    tab = []
    for i in range(1, n):
        if n%i==0:
            tab.append(i)
    return tab

print(czynniki_pierwsze(5))
print(czynniki_pierwsze(10))
print(czynniki_pierwsze(20))
print(czynniki_pierwsze(100))
