import numpy as np

'''
Aplikacja wydająca resztę...
Nominały do wydawania: 500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1
np. 
kw = 151.20
wp = 200
r = wp-kw = 200 - 151.20 = 48.80
'''

nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
dowyplaty = {}

#menu
def menu():
    print("=" * 50)
    print("Aplikacja do wydawania reszty")
    print("=" * 50)

# wyświetlanie wyników
def show(dowyplaty):
    if isinstance(dowyplaty, dict):
    # if type(dowyplaty) is dict:
        print("Nominały do wypłaty: ")
        for k, v in dowyplaty.items():
            if v != 0:
                print(f"{k} PLN - {v} sztuk")
    else:
        print(dowyplaty)
# wprowadzanie wartości kw i wp
def entry():
    try:
        kw, wp = -1, -2
        while kw <= 0 or wp <= 0 or kw > wp or kw != np.round(kw,2) or wp != np.round(wp,2):
            kw = float(input("Podaj kwotę do zapłaty: "))
            wp = float(input("Podaj wartość wpłaty: "))
            if kw <= 0 or wp <= 0:
                print("Podałeś ujemną liczbę. Wprowadź ponownie: ")
            if kw > wp:
                print("Podałeś mniejszą kwotę wpłaty od należnej. Podaj ponownie: ")
            if kw != np.round(kw,2) or wp != np.round(wp,2):
                print("Podana wartość powinna mieć tylko dwa miejsca po przecinku.")
            
    except ValueError:
        print("Nie podałeś liczb!")
    else:
        dowyplaty = wydaj(kw, wp)
        show(dowyplaty)
        
# wydawanie reszty
def wydaj(kw, wp):
    r = wp - kw
    if r != 0:
        i = 0
        while r != 0 and i < len(nominaly):
            ile = int(r / nominaly[i])
            r -= ile * nominaly[i]
            r = np.round(r,2)
            dowyplaty[nominaly[i]] = ile
            i += 1
        return dowyplaty
    else:
        return "Nic do wydania."
# ---------------------------------
def main():
    while True:
        menu()
        entry()
        koniec = input("Czy chcesz kontynuować? (t/n)")
        if koniec in ('t', 'n', 'T', 'N'):
            if koniec != 't' and koniec != 'T':
                print("_____________ Dziękuję za współpracę ____________")
                break
        else:
            print("Zły wybór łosiu!!!")
        

if __name__ == "__main__":
    main()   


    