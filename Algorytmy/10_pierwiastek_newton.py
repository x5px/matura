epsilon = 0.000001

def newton(P, epsilon):
    a, b = 1, P

    while(abs(a-b) >= epsilon):
        a = (a+b)/2
        b = P/a
    return (a+b)/2


p = int(input("Podaj liczbę którą chcesz pierwiastkować: "))

print(newton(p, epsilon))