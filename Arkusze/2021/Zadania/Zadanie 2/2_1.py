def d(T, x):
    n = len(T)
    for i in range(0, x):
        T.append(0)
    s = n+1
    while(s // 2 >= 1 and T[s] > T[s // 2]):
        pom = T[s]
        T[s] = T[s // 2]
        T[s // 2] = pom
        s = s // 2
    return T

print(d([26, 3, 5, -4], 5))