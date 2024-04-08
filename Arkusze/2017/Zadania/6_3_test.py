tab = []
file = open('../Dane_PR/przyklad.txt', 'r')
for line in file:
    tab.append(line.split())
file.close()

result = []

for i in range(200):
    for j in range(319):
        if abs(int(tab[i][j]) - int(tab[i][j + 1])) > 128:
            if [i, j] not in result:
                result.append([i, j])
            if [i, j + 1] not in result:
                result.append([i, j + 1])

for i in range(199):
    for j in range(320):
        if abs(int(tab[i][j]) - int(tab[i + 1][j])) > 128:
            if [i, j] not in result:
                result.append([i, j])
            if [i + 1, j] not in result:
                result.append([i + 1, j])

print(len(result))
print(result)
