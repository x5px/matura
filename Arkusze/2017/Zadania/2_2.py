ct = 0

def licz(x):
    global ct
    if x==1:
        ct += 1
        return ct
    else:
        w = licz(x//2)
        if x%2==1:
            ct += 1
            return w+1
        else:
            ct += 1
            return w-1

for i in range(1, 20):
    print(i, licz(i))