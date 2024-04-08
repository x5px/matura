'''
Jakub R
Matura 2023 Próbna CKE
Zadanie nr 1.2
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
        ct += 2
        return x+z+z

print(iloczyn(9, 11))
print(ct)
ct = 0

print(iloczyn(8, 32))
print(ct)
ct = 0

print(iloczyn(2, 47))
print(ct)
ct = 0


print(iloczyn(112, 112))
print(ct)
ct = 0

