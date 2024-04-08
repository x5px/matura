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

def znajdzNajwiecejNieparzystych(przedzialy):
    counts = []
    for i in przedzialy:
        counter = 0
        for liczba in i:
            if liczba %2 != 0:
                counter += 1
        counts.append((i, counter))

    num_count= [i[1] for i in counts]
    max_v = max(num_count)

    for i in range(0, len(counts)):
        if num_count[i] == max_v:
            print(i+1, max_v)


przedzialy = get_przedzialy('przedzialy')
# print(przedzialy)
znajdzNajwiecejNieparzystych(przedzialy)