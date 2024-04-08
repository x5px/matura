'''
Jakub R
Matura 2023 Próbna CKE
Zadanie nr 1.1
'''
ct = 0

def iloczyn(x, y):
    global ct
    if y == 1:
        return x
    else:
        k = y//2
        z = iloczyn(x, k)
    if y%2==0:
        ct += 1
        return z+z
    else:
        ct += 1
        return x+z+z

print(iloczyn(10, 45))

