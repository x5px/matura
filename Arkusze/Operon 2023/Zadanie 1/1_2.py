import math

def conv2dec(num, base):
    #print(f"Liczba {num} w podstawie {base}")
    #print("---------------")
    decnum = 0
    base = int(base)
    hex_dict = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }
    num = num[::-1]
    for i in range(0, len(num)):
        if num[i] in hex_dict:
            current_num = hex_dict[num[i]]
        else:
            current_num = int(num[i])
        #print(f"{decnum} + {current_num*(base**i)} (base: {base}, i: {i}, pot: {base**i})")
        decnum += current_num*(base**i)
    return decnum

def isSym(num):
    num = str(num)
    mid = math.ceil(len(num) / 2)
    if(len(num) % 2 == 0):
        left = num[0:mid]
        right = num[mid:][::-1]
    else:
        left = num[0:mid-1]
        right = num[mid:][::-1]

    if left == left[::-1] and right == right[::-1]:
        return True
    else:
        return False

with open('../dane/symetryczne.txt', 'r') as plik:
    out = plik.readlines()

lines = []

for line in out:
    lines.append(line.strip().split(' '))

dec = []

for i in range(0,len(lines)):
    dec.append(conv2dec(lines[i][1], lines[i][0]))

print(len(list(filter(isSym, dec))))