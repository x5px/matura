'''
Jakub R
Matura 2023 Próbna CKE
Zadanie nr 2.4
'''

def loadfile(filename):
	t = []
	with open(f'../../DANE/DANE_M/{filename}.txt') as f:
		for i in f.readlines():
			t.append(i.strip())
	return t

def anagram(tab):
	res = []
	for i in tab:
		kombinacje = []
		for j in range(0, len(i)):
			for k in range(0, len(i)):
				kombinacje.append((i[j], i[k]))