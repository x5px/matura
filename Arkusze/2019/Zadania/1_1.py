def b_sort(tab):
    for i in range(0, len(tab)):
        for j in range(0, len(tab)):
            if tab[i] < tab[j]:
                tab[i], tab[j] = tab[j], tab[i]
    return tab

# def bin_search(tab, n):
#     # low = 0
#     # high = n
#     # mid = int(high//2)
#     #
#     # A = tab[:mid]
#     # B = tab[mid:]
#     #
#     # return [(A[:len(A)//2], A[len(A)//2:]), (B[:len(B)//2], B[len(B)//2:]) ]
#     #
#     B = []
#
#     for i in range(0, int(n**(1/2))):
#         low = 0
#         mid_A = int(len(A)//2)
#         mid_B = int(len(B)//2)
#         print(A[:mid_A], A[mid_A:])
#         B = A[mid_A:]


def pierwsza(A, n):
    ct = 0
    i = 0
    m = n-1
    while i<m:
        pivot = int((i+m)/2)
        if A[pivot] % 2 == 0:
            m = pivot
        else:
            i = pivot + 1
    return A[m]

n = 10
A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]

#print(b_sort(A))
print(pierwsza(A, n))