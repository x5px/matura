'''
Jakub R
Matura 2017
Zadanie nr 6.5
'''

def loadfile(filename):
    with open(f"../Dane_PR/{filename}.txt") as f:
        tab = []
        for i in f.readlines():
            i = i.split(' ')
            for j in range(0, len(i)):
                i[j] = int(i[j])
            tab.append(i)

    return tab

def kolumny(tab):
    kol = list(zip(*tab))

    return kol

# uwaga: duża złożoność obliczeniowa

# def find_max_len(tab):
#     ct = 0
#     mytab = []
#     i_new = 0
#     j_new = 0
#     for i in range(0, len(tab)):
#         for j in range(0, len(tab[0])):
#             for k in range(0, len(tab[0])):
#                 if len(list(set(tab[i][j:k]))) == 1 and len((tab[i][j:k])) > ct:
#                     ct = len((tab[i][j:k]))
#     return ct

def find_max_len(tab):
    long_tab = [i for row in tab for i in row] # mądre!

    max_ct = 0
    # return long_tab

    for i in range(0, len(tab)):
        ct = 0
        for j in range(0, 200):
            # print(i*j)
            if long_tab[i*j] == long_tab[i*j+1]:
                ct += 1
            else:
                if ct > max_ct:
                    max_ct = ct
                ct = 0
        # print("-------------")
    # print(len(long_tab))

    return max_ct+1


tab = loadfile('przyklad')
d_tab = loadfile('dane')



print(find_max_len(kolumny(tab)))
# print(find_max_len(kolumny(d_tab)))