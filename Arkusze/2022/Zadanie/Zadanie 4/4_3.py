import itertools
def trojka(x, y, z, a=None, b=None):
    if a is not None: # piątki
        tab = [x, y, z, a, b]
        if len(list(set(tab))) != 5:
            return False
        else:
            for i in range(1, 5):
                if(tab[i] % tab[i-1] != 0):
                    return False
        return True
    else:
        return x != y and x != z and y != z and y%x==0 and z%y==0 # trójki


# def n_length_combo(iterable, r): # przerobić w domu
#     char = tuple(iterable)
#     n = len(char)
#
#     if r > n:
#         return
#
#     index = numpy.arange(r)
#
#     # returns the first sequence
#     yield tuple(char[i] for i in index)
#
#     while True:
#
#         for i in reversed(range(r)):
#             if index[i] != i + n - r:
#                 break
#         else:
#             return
#
#         index[i] += 1
#
#         for j in range(i + 1, r):
#             index[j] = index[j - 1] + 1
#
#         yield tuple(char[i] for i in index)

def sprawdz_trojki(filename):
    txt = []
    with open(f'../../Dane_2205/{filename}.txt') as f:
        for i in f.readlines():
            txt.append(int(i.replace('\n', '')))

    # trojki = []
    # for i in range(0, len(txt)):
    #     for j in range(i, len(txt)-i):
    #         for k in range(i+j+2, len(txt)-i-j):
    #             # if(txt[i] == txt[j] or txt[i] == txt[k] or txt[j] == txt[k]):
    #             #     print(f"{txt[i]} vs {txt[j]} vs {txt[k]}")
    #             trojki.append([txt[i], txt[j], txt[k]])
    # print(trojki)
    dobre_t = 0
    dobre_p = 0
    #trojki = itertools.permutations(txt, 3)
    piatki = itertools.permutations(txt, 5)
    print(list(piatki))


    #
    # for t in trojki:
    #     if trojka(t[0], t[1], t[2]):
    #         dobre_t += 1
    # # for p in piatki:
    # #     if trojka(t[0], t[1], t[2], t[3], t[4]):
    # #         dobre_p += 1
    # return (dobre_t, dobre_p)
    # #print(len(trojki))
# print(trojka(2, 6, 12)) # T
# print(trojka(2, 10, 12)) # F

print(sprawdz_trojki('przyklad'))