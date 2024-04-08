# wsp - współczynniki
# w_x - wielomian
def horner_iter(wsp, x):
    i = 0
    w_x = 0
    for i in wsp:
        w_x = w_x*x + i
    return w_x

def horner_reku(wsp, stopien, x):
    if(stopien == 0):
        return wsp[0]
    return x * horner_reku(wsp, stopien-1, x) + wsp[stopien]

# wsp = input("Podaj wielomian: ")
# x = int(input("Podaj współczynnik wielomianu: "))

# [1, 2, 5, 1] = x^4+2x^3+5x+1
print(horner_iter([1, 2, 5, 1], 2))
print(horner_reku([1, 2, 5, 1], len([1, 2, 5, 1])-1, 2))
# index 0 to potęga 1 a nie 0