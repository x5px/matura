def algo(n):
    w = 0
    while n!=0:
        w = w + (n%10)
        print(w)
        n = n // 10
    print("-------")
    return w

print(algo(11111))