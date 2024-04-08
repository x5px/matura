'''
Jakub R
Matura 2023 Próbna CKE
Zadanie nr 2.1
'''

def czy_mniejszy(n, s, k1, k2):
    ct = 0
    i = k1-1
    j = k2-1
    while ( i <= n-1 and j <= n-1 ):
        #print(i, j)
        if(s[i] == s[j]):
            print(f"Sprawdzenie s[{i+1}]  vs s[{j+1}]")
            ct += 1
            i = i + 1
            j = j + 1
        else:
            print(f"{s[i]} to nie jest {s[j]}")
            return ct
    return ct
        # 	if (s[i] < s[j]):
        # 		return True
        # 	else:
        # 		return False
        # if( j <= n ):
        # 	return True
        # else:
        # 	return False

print(czy_mniejszy(10,'aaaaaaabcd', 1, 2))
#print(czy_mniejszy(len('ababababb'),'ababababb', 1, 3))
#print(czy_mniejszy(len('aaaaaaaaaa'),'aaaaaaaaaa', 2, 5))

# print(czy_mniejszy(10, 'mascarpone', 5, 2))