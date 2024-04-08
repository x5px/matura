'''
Jakub R
Matura 2023 Próbna CKE
Zadanie nr 3.1
'''

def loadfile(filename):
	t = []
	with open(f'../../DANE/DANE_M/{filename}.txt') as f:
		for i in f.readlines():
			t.append(i.strip())
	return t

def anagram(tab):
	zrown = 0
	prawie = 0
	for i in tab:
		ct_0 = 0
		ct_1 = 0
		for j in i:
			if j == '0':
				ct_0 += 1
			if j == '1':
				ct_1 += 1
		if ct_0 == ct_1:
			zrown += 1
		if abs(ct_1-ct_0) == 1:
			prawie += 1
	print(zrown)
	print(prawie)


# tab = loadfile('przyklad')
tab = loadfile('anagram')
anagram(tab)
