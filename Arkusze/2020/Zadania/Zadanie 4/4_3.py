with open('pary.txt', 'r') as f:
    tab = f.readlines()

new_tab = []
for i in tab:
    new_tab.append(i.replace('\n', '').split(' '))

pary = []
for i in new_tab:
    if (int(i[0]) == len(i[1])):
        pary.append(i[1])

print(str(len(sorted(pary)[0])) + ' ' + sorted(pary)[0])