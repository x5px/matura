def suma(a):
    S = 1
    k = 2
    while(a>k*k):
        if a % k == 0:
            S += k
            S += a // k
        # print(a)
        k += 1
    #print(k)
    if a%k == 0:
        S += k

    return S

def zaprzyjaznione(a, b):
    if(suma(a)) == b and suma(b) == a:
        return True
    else:
        return False

print(zaprzyjaznione(220, 284)) # T
print(zaprzyjaznione(284, 220)) # T
print(zaprzyjaznione(21, 37)) # F
print(zaprzyjaznione(4, 20)) # F

