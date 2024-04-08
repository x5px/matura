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



