with open('pary.txt', 'r') as f:
    tab = f.readlines()

new_tab = []
for i in tab:
    new_tab.append(i.replace('\n', '').split(' '))

litery = [new_tab[i][1] for i in range(len(new_tab))]

for txt in litery:
    if len(txt) == 1:
        print(txt)
    else:
        ciag = ''
        ciag_new = ''
        max_len = -1
        for i in range(0, len(txt)-1):
            if(txt[i] == txt[i+1]):
                ciag_new += txt[i]
            # if(i == len(txt)-1 and txt[i] == txt[i-1]):
            #     ciag_new += txt[i+1]
            else:
                if len(ciag_new) > max_len:
                    ciag = ciag_new
                    max_len = len(ciag_new)
                ciag_new = ''
        if ciag == '':
            ciag = txt[0]
        else:
            ciag += ciag[-1]
        print(ciag, len(ciag))