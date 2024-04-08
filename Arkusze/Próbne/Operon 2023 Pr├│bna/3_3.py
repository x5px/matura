alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def b_sort(tab):
    for i in range(len(tab)-1):
        for j in range(0, len(tab)-1-i):
            if(tab[j] > tab[j+1]):
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

def sortWord(txt):
    chartab = []
    new_txt = ''
    for i in txt:
        chartab.append(alfabet.index(i))
    chartab = b_sort(chartab)
    for i in chartab:
        new_txt += alfabet[i]
    return new_txt

def anagram(txt, txt2):
    if sortWord(txt) == sortWord(txt2):
        return True
    else:
        return False

def findMaxAnagram(filename):
    txts = []
    with open(f'{filename}.txt', 'r') as f:
        for i in f.readlines():
            txts.append(i.replace('\n', ''))

    anagrams = [[i, 0] for i in txts]
    #print(anagrams)
    for i in range(0, len(txts)):
        for j in range(0, len(txts)):
            #print(f"{txts[i]} vs {txts[j]}")
            if txts[i] != txts[j] and anagram(txts[i], txts[j]):
                anagrams[i][1] += 1
    #print(anagrams)
    max_v = max([i[1] for i in anagrams])
    for i in anagrams:
        if i[1] == max_v:
            search_for = i[0]
            break

    list_all = []
    for i in range(0, len(txts)):
        if(anagram(txts[i], search_for)):
            list_all.append(txts[i])
    return list_all

    #print(len(list_all) == len(list(set(list_all))))
    # sprawdzenie

print(findMaxAnagram('anagramy'))