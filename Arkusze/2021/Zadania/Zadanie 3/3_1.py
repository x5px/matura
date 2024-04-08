def f(n):
    if n > 0:
        print(n)
    print(n)
    return f(n-2)

print(f(5))
print(f(6))
print(f(7))
print(f(8))