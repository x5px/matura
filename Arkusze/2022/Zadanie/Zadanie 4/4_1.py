'''
Zadanie 4.1

'''

def pierwsza_ostatnia():
    with open('../../Dane_2205/liczby.txt', 'rt') as f:
        txt =  [i.replace('\n', '') for i in f.readlines()]

    count = 0
    first = ""

    for i in txt:
        if i[0] == i[-1]:
            if first == "":
                first = i
            count += 1
    return (count, first)

print(pierwsza_ostatnia())