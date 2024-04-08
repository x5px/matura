'''
Jakub R
Matura 2023 Próbna CKE
Zadanie nr 2.4
'''

def loadfile(filename):
	t = []
	with open(f'../../DANE/DANE_M/{filename}.txt') as f:
		for i in f.readlines():
			t.append(i.strip().split(' '))
	return t


def czy_mniejszy(n, s, k1, k2):
	# print(f"Czy_mniejszy: {k1}, {k2}")
	# print(n, s, k1, k2)
	i = k1
	j = k2
	while ( i <= n-1 and j <= n-1 ):
		# print(s[i])
		# print(s[j])
		if(s[i] == s[j]):
			i = i + 1
			j = j + 1
		else:
			if (s[i] < s[j]):
				return True
			else:
				return False
	if( j <= n ):
		return True
	else:
		return False

def sort_tab(s, n):
	tab = []
	for i in range(0, len(s)):
		tab.append((s[i:], i))

	for i in range(0, len(s)):
		for j in range(0, len(s)):
			if i!=j:
				if czy_mniejszy(n, s, tab[i][1], tab[j][1]):
					tab[i], tab[j] = tab[j], tab[i]

	return tab[0][0]


# tab = loadfile('sufiks_4')
tab = loadfile('slowa4')
for i in range(0, len(tab)):
    n = int(tab[i][0])
    print(sort_tab(tab[i][1], n))