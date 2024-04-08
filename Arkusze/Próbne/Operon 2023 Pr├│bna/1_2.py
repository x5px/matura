def get_przedzialy(filename):
    lines = []
    przedzialy = []

    with open(f'{filename}.txt', 'r') as f:
        for i in f.readlines():
            lines.append(i.replace('\n', '').split(','))
    for i in lines:
        l_zamkn = False
        p_zamkn = False

        if i[0][0] == '<':
            l_zamkn = True
        if i[1][-1] == '>':
            p_zamkn = True

        ranges = (int(i[0].replace('<', '').replace('>', '').replace('(', '').replace(')', '')), int(i[1].replace('<', '').replace('>', '').replace('(', '').replace(')', '')))
        #print(ranges, l_zamkn, p_zamkn)

        # range liczy od startu włącznie do end-1
        r_start = ranges[0] # range start/end
        if not l_zamkn:
            r_start += 1
            #r_start -= 1
            pass
        r_end = ranges[1]
        if p_zamkn:
            r_end += 1
        #
        # print(r_start, r_end)

        przedzialy.append([i for i in range(r_start, r_end)])

    return przedzialy
def sito(n):
    tab = [True] * (n+1)
    for i in range(2, int(n**(1/2))):
        if tab[i]:
            for j in range(i*i, n+1, i):
                tab[j] = False

    return [i for i in range(2, len(tab)) if tab[i] == True]

def znajdzNajwiecejPierwszych(przedzialy):
    counts = []
    for przedzial in przedzialy:
        counter = 0
        for i in range(0, len(przedzial)):
            przedzial[i] = abs(przedzial[i])

        pierwsze = sito(max(przedzial))

        for i in range(0, len(przedzial)):
            if i in pierwsze:
                counter += 1
        counts.append([przedzial, counter])

    max_v = max([counts[i][1] for i in range(len(counts))])
    #print(max_v)

    lines = []
    with open('przedzialy.txt', 'r') as f:
        for i in f.readlines():
            lines.append(i.replace('\n', ''))

    for i in range(0, len(counts)):
        if counts[i][1] == max_v:
            print(lines[i])

przedzialy = get_przedzialy('przedzialy')

znajdzNajwiecejPierwszych(przedzialy)