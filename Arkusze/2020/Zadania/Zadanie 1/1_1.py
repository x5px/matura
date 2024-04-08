def czy_k_podobne(n, A, B, k):
    for i in range(k):
        if(A[i] != B[i+n-k]):
            return False
    for i in range(n-k):
        if(A[k+i] != B[i]):
            return False
    return True

print(czy_k_podobne(3, [5,7,9], [5,7,9], 0))

print(czy_k_podobne(5, [4,7,1,4,5], [1,4,5,4,7], 2))

print(czy_k_podobne(5, [10, 9, 12, 10, 9], [10, 10, 9, 9, 12], 3))

print(czy_k_podobne(5, [1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 2))

