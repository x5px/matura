'''
Skrót przydatny na maturę
#3 - podzbiory zbioru
Jakub Rutkowski 2024
'''

def subsets(s):
    if not s:
        return [[]]
    return subsets(s[1:])+[[s[0]]+x for x in subsets(s[1:])]

print(subsets([1,2,3])) # [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]