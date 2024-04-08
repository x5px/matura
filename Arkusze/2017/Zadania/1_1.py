def b_sort_reverse(tab):
    for i in range(0, len(tab)):
        for j in range(0, len(tab)):
            if tab[i] > tab[j]:
                tab[i], tab[j] = tab[j], tab[i]
    return tab

def pole(A, p):
    A = list(set(A))
    A = [x for x in A if x%p!=0]

    if len(A) < 2:
        return 0
    A = b_sort_reverse(A)
    # print(A)
    return A[0] * A[1]


print(pole([7, 5, 11, 33], 3))
print(pole([15, 12, 10, 6, 5, 1], 5))
print(pole([6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18], 7))
print(pole([4, 34, 16, 8, 6, 22, 14, 12, 2, 7], 2))
