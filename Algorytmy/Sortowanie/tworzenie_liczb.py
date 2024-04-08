'''
Plik do tworzenia pliku liczby.txt
przechowującego 1000 liczb z zakresu
-10000 do 10000
'''

import random as rd

n = int(input("Ile liczb chcesz wygenerować? "))
d = int(input("Podaj dolny zakres: "))
g = int(input("Podaj górny zakres: "))
if d>g:
    d,g = g,d
    
with open("liczby.txt", "w+") as f:
    for i in range(n):
        liczba = rd.randint(d, g)
        f.write(str(liczba)+"\n")

