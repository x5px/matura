def sym(a, b):
    if a==0:
        return 0
    else:
        sym(a-1, b+1)
        print(a*b, end=' ')
        sym(a-1, b+1)

sym(3,1)
print()
sym(4,2)
print()
sym(3,3)
print()
sym(4,1)
print()
sym(5, 1)
