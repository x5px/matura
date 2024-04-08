def loadfile(filename):
    with open(f'../Dane_PR/{filename}.txt') as f:
        tab = []
        for l in f.readlines():
            l = int(l.replace('\n', ''))
            tab.append(l)
    return tab

def find_powers(tab):
    power_rangers = [3**i for i in range(0, int((max(tab))**(1/3)))]
    ct = 0
    for i in tab:
    #     str_i = str(i)
    #     for j in str_i:
    #         suma_liczb += int(j)
    #     if suma_liczb % 3 == 0 and int(str_i[-1]) in [3, 7, 9, 1]:
    #         print(i, suma_liczb)
    #         ct += 1
        if i in power_rangers:
            ct += 1
    return ct


# print(find_powers(loadfile('przyklad')))
print(find_powers(loadfile('liczby')))
