'''
Jakub R
Matura 2023 Próbna CKE
Zadanie nr 1.3
'''

def iloczyn(x, y):
    global ct
    if y == 1:
        return x
    else:
        k = y//2
        z = iloczyn(x, k)
    if y%2==0:
        return z+z
    else:
        return x+z+z

def iloczyn_iter(x, y):
    z = 0
    while(y != 0):
        if y%2==1:
            z = x+z
        x = x+x
        y = y//2

    return z

print(iloczyn_iter(2, 3))
print(iloczyn_iter(10, 45))
print(iloczyn_iter(100, 100))
