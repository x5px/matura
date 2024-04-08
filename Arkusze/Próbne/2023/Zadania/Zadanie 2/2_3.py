'''
Jakub R
Matura 2023 Próbna CKE
Zadanie nr 2.3
'''

def loadfile(filename):
	with open(f'../../DANE/DANE_M/{filename}.txt') as f:
		t = [i.strip() for i in f.readlines()]
		t[0] = int(t[0])
		t[2] = [int(i) for i in t[2].split(' ')]

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
		tab.append(i)

	for i in range(0, len(s)):
		for j in range(0, len(s)):
			if i!=j:
				if czy_mniejszy(n, s, tab[i], tab[j]):
					tab[i], tab[j] = tab[j], tab[i]

	return [i+1 for i in tab]

print(sort_tab('mascarpone', 10))
print(sort_tab('kalafiorowa', 11))