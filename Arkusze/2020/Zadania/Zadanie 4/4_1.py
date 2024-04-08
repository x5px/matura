import math
import sys


# def czy_pierwsza(n):
#     tab = [True] * (n+1)
#     for i in range(2, int(math.ceil(math.sqrt(n)))+1):
#         for j in range(i*i, n+1, i):
#             tab[j] = False
#     tab.pop(0) # 0
#     tab.pop(0) # 1
#     return tab

def czy_pierwsza(n):
    if n in [0, 1]:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    return True

# for i in range(0, 20):
#     print(str(i) + ' ' + str(czy_pierwsza(i)))

def goldbach(n):
    if(n<=4 or n%2 != 0):
        return
    max_rozn = -sys.maxsize
    nums = []
    for i in range(2, n):
        for j in range(2, n):
            # print(j, i, j - i)
            if(czy_pierwsza(i) and czy_pierwsza(j) and j-i > max_rozn and abs(i+j) == n):
                nums = (i, j)
                max_rozn = j-i
    print(str(n) + ' ' + str(nums[0]) + ' ' + str(nums[1]))
# print(goldbach(20)) # 20 3 17
# print(goldbach(24)) # 24 5 19
# print(goldbach(6)) # 6 3 3

tab = []
with open('pary.txt', 'r') as f:
    tab = f.readlines()

new_tab = []
for i in tab:
    new_tab.append(i.replace('\n', '').split(' '))

liczby = [int(new_tab[i][0]) for i in range(len(new_tab))]

for i in liczby:
    goldbach(i)