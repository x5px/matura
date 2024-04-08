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

print(suma(220))
print(suma(284))
