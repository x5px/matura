def loadfile(filename):
    with open(f'../Dane_PR/{filename}.txt') as f:
        tab = []
        for l in f.readlines():
            l = int(l.replace('\n', ''))
            tab.append(l)
    return tab
def nwd(a, b):
    while(a != 0 and b != 0):
        if a>=b:
            a = a-b
        if b>a:
            b = b-a
    return max(a, b)

def find_nwd_seq(tab):
    ciag_tab = []
    for i in range(0, len(tab)-1):
        # print(i, " ", i+1)
        if nwd(tab[i], tab[i+1]) > 1:
            ciag_tab.append(i)

    ciag = []
    c_nwd = 0
    max_ciag = []
    # for i in ciag_tab:
    #     # print(tab[i], " ", tab[i+1], " ", nwd(tab[i], tab[i+1]))
    #     if nwd(tab[i], tab[i+1]) > 1:
    #         ciag.append(tab[i])
    #         c_nwd = nwd(tab[i], tab[i+1])
    #         # print(ciag)
    #     else:
    #         ciag = []
    #     if len(ciag) > len(max_ciag):
    #         max_ciag = ciag
    #
    # ind = tab.index(max_ciag[-1])
    # try:
    #     if(nwd(tab[ind], tab[ind+1])) > 1:
    #         max_ciag.append(tab[ind+1])
    # except ValueError:
    #     pass
    #
    # print(max_ciag[0], len(max_ciag), c_nwd)



# print(nwd(24, 30))
# print(nwd(128, 96))

tab = loadfile('przyklad')
print(find_nwd_seq(tab))
#
#
# find_nwd_seq([3, 7, 4, 6, 10, 2, 5])
# find_nwd_seq([5, 70, 28, 42, 98])