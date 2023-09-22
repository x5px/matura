"""
MATURA 2023
Jakub Rutkowski

# 3 - Palindromy (Szybkie wyszukiwanie)

Palindrom - wyraz, który czytany wspak jest nadal taki sam

Działanie algorytmu:
1. Bierzesz początkowy i końcowy znak wyrazu i je porównujesz.
2. Jeżeli nie są równe, zwróć False.
3. Jeżeli są równe, powtórz dla następnych w zdaniu.
4. Jeśli dojdziesz do środkowego znaku lub nie ma już znaków do sprawdzenia, zwróć True.
"""

def palindrom(wyraz):
    dl = len(wyraz)

    if dl %2 != 0:
        for i in range(1, dl//2):
            if(wyraz[i-1] != wyraz[-i]):
                #print(wyraz[i-1], wyraz[-i])
                return False
        return True
    else:
        for i in range(1, dl):
            if (wyraz[i-1] != wyraz[-i]):
                return False
        return True

print(palindrom("aabaa")) # True
print(palindrom("abcde")) # False
print(palindrom("aaaaa")) # True
print(palindrom("aabbaa")) # True


