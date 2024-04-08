def NWD(a, b): 
    k = 1
    while b != 0:
        k = b
        b = a%b
        a = k
    return a

def spr(linie):
    pom = [] 
    dzielnik = int(linie[0]) 
    maxPierwsza = 0 
    maxDlugosc = 0 
    maxDzielnik = 1 

    for i in range(1, 500): 
        num = int(linie[i]) 
        nwd = NWD(dzielnik, num) 
        if nwd != 1: 
            if len(pom) == 0: 
                pom.append(dzielnik) 
            pom.append(num) 
            dzielnik = nwd 
        else:
            if len(pom) > maxDlugosc:
                maxDlugosc = len(pom) 
                maxDzielnik = dzielnik
                maxPierwsza = pom[0] 
            if len(pom) != 0: 
                if NWD(pom[len(pom)-1], num) > 1:
                    a = pom[len(pom)-1] 
                    pom.clear() 
                    pom.append(a) 
                    pom.append(num) 
                else:
                    pom.clear() 
            dzielnik = num
    print(f"Pierwsza: {maxPierwsza} dzielnik: {maxDzielnik} dlugość: {maxDlugosc}")
    
    

with open("../Dane_PR/liczby.txt", "r") as file:
    linie = file.read().splitlines() 
    
spr(linie)
