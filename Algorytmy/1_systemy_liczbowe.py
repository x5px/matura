"""
MATURA 2024
Jakub Rutkowski

#1 - Systemy liczbowe

Dziesiętne
Binarne
Oktagonalne
Szesnastkowe
"""

hex_dict = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def dec2base(n, base):

    new_str = ''
    while n != 0:
        r = n % base
        if r > 9:
            new_str += hex_dict[r]
        else:
            new_str += str(r)
        n = n // base
    return new_str[::-1]

def base2dec(n, base):
    n = str(n)[::-1]
    num = 0
    for i in range(0, len(str(n))):
        if(n[i] not in hex_dict.values()):
            num += int(n[i]) * base ** i
        else:
            num += int(hex_dict[(list(hex_dict.values()).index("F")+10)]) * base ** i
    return num

def show_menu():
    print("=" * 30)
    print("Systemy liczbowe")
    print("=" * 30)
    print()
    while(1):
        print("Wybierz tryb")
        print("1 - dziesiętne -> inny system")
        print("2 - inny system -> dziesiętne")
        print("c - wyjdź")
        mode = input()
        print("Wybrano: ", mode)
        if mode == '1':

            n = int(input("Podaj liczbę dziesiętną: "))
            base = int(input("Podaj podstawę drugiego systemu: "))
            print(dec2base(n, base))
        elif mode == '2':
            n = int(input("Podaj liczbę w innym systemie: "))
            base = int(input("Podaj podstawę tego systemu: "))
            print(base2dec(n, base))
        elif mode == 'c':
            break
        else:
            print("Zły wybór")

show_menu()


