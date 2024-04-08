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

def b_sort(tab):
    for i in range(len(tab)-1):
        for j in range(0, len(tab)-1-i):
            if(tab[j] > tab[j+1]):
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

def get_total_sum(przedzialy):
    total = []
    for i in przedzialy:
        total.extend(i)
    total = b_sort((list(set(total)))) # usun duplikaty, sortuj
    #print(total)
    count = []
    max_count = []
    for i in range(0, len(total)-1):
        if total[i] + 1 == total[i+1]:
            count.append(total[i])
        else:
            #print(f"{total[i]} vs {total[i+1]}")
            if len(count) >= len(max_count):
                max_count = count
            count = []

    print('<' + str(min(max_count)) + ',' + str(max(max_count)) + '>')

przedzialy = get_przedzialy('przedzialy')
get_total_sum(przedzialy)