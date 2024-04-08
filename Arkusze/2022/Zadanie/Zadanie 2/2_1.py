def abslowo(s, n):
    A = [0] * n
    B = [0] * n

    # print(n)
    # print(len(B))

    for i in range(0, n):
        if s[i] == 'a':
            A[i] = A[i-1] + 1
        else:
            A[i] = A[i-1]
    B[n-1] = 0
    for j in range(n-2, 0, -1):
        if(s[j] == 'b'):
            B[j] = B[j+1] +1
        else:
            B[j] = B[j+1]
    k=1
    for i in range(0, n-1):
        if(A[i] + B[i+1] > k):
            k = A[i] + B[i+1]

    return k+1

print(abslowo('aabab', 5))
print(abslowo('ab', 2))
print(abslowo('aaa', 3))
print(abslowo('aababb', 6))
print(abslowo('baabbaaab', 9))

