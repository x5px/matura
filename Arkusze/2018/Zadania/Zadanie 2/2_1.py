# X = [-2, 1, 3, 2]
# Y = [2, 3, 4, 1]

X = [1, 2, 3, -2]
Y = [3, 1, 4, 2]

for i in range(0, len(X)-1):
    for j in range(1, len(X)):
        if X[i]/Y[i] > X[j]/Y[j]:
            X[i], X[j] = X[j], X[i]
            Y[i], Y[j] = Y[j], Y[i]
            # print(X)
            # print(Y)

print(X[0], Y[0])