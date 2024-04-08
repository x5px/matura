# def findBiggestDop():
#     tab_d = []
#     for i in range(1000, 9000):
#         temp = []
#         for j in str(i):
#             temp.append(str(int(9 - int(j))))
#         tab_d.append((i, int(''.join(temp))))
#         temp.clear()
#     d = [abs(tab_d[i][0] - tab_d[i][1]) for i in range(0, len(tab_d))]
#     return (tab_d[d.index(max(d))][0], max(d))

# def findSmallestDop():
#     tab_d = []
#     for i in range(1000, 9000):
#         temp = []
#         for j in str(i):
#             temp.append(str(int(9 - int(j))))
#         tab_d.append((i, int(''.join(temp))))
#         temp.clear()
#     d = [abs(tab_d[i][0] - tab_d[i][1]) for i in range(0, len(tab_d))]
#     return (tab_d[d.index(min(d))][0], min(d))

def findBiggestDopAlgo():
    tab_d = []
    for i in range(1000, 9000):
        temp = 0
        for j in range(4, 0, -1):
            # print(10**j)
            temp += (i % 10**j)
            i = i // 10**j
        tab_d.append((i, temp))
    d = [abs(tab_d[i][0] - tab_d[i][1]) for i in range(0, len(tab_d))]
    return (tab_d[d.index(max(d))][0], max(d))

def findSmallestDopAlgo():
    tab_d = []
    for i in range(1000, 9000):
        temp = 0
        for j in range(4, 0, -1):
            # print(10**j)
            temp += (i % 10**j)
            i = i // 10**j
        tab_d.append((i, temp))
    d = [abs(tab_d[i][0] - tab_d[i][1]) for i in range(0, len(tab_d))]
    return (tab_d[d.index(min(d))][0], min(d))

# print(findSmallestDop())
# print(findBiggestDop())

print(findSmallestDopAlgo())
print(findBiggestDopAlgo())