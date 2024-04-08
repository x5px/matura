# Zadanie 3.3 Matura 2023

def sequence(i):
    seq = []  # rozdzielenie na możliwe ciągi
    for j in [2, 3, 4]:
        seq.append([i[:j], i[j:]])
    return seq

def sprawdz_ros_mal(ciag):
    ros = True
    mal = True

    for i in range(0, len(ciag)-1):
        if ciag[i] > ciag[i+1]:
            mal = False
        if ciag[i] < ciag[i + 1]:
            ros = False

    if ros:
        return -1
    if mal:
        return 1
    else:
        return 0


def ciagi(tab):
    frag = []
    for i in range(0, len(tab)-5):
        frag.append([tab[i], tab[i+1], tab[i+2], tab[i+3], tab[i+4], tab[i+5]])

    ct = 0
    for i in frag: # fragment tekstu
        for j in sequence(i): # dla każdego zestawu ciągów
            res1 = sprawdz_ros_mal(j[0])
            res2 = sprawdz_ros_mal(j[1])

            if res1 == 1 and res2 == -1:
                print(i)
                print(j[0], j[1], res1, res2)
                ct += 1
                break

    print(ct)


with open('../../Dane_2305/pierwsze10.txt') as f:
    liczby = [int(i.replace('\n','')) for i in f.readlines()]

ciagi(liczby)

# print(sprawdz_ros_mal([1, 5,6, 8])) #1
# # print(sprawdz_ros_mal([1, 5, 6, 8]))
# print(sprawdz_ros_mal([8, 6, 5, 3])) #-1