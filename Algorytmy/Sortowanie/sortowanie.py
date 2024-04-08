'''
Sortowanie liczb różnymi metodami
K>K> 2023
'''

import time
from random import randint as rdi

# menu
def menu():
    print("""
        b - bubble sort,
        i - insert sort,
        s - selection sort,
        q - quick sort
    """)

# funkcja dekoratora pomiaru czasu
def measuretime(func):
    def wrapper(*kwargs):
        starttime = time.perf_counter()
        liczby = func(*kwargs)
        stoptime = time.perf_counter()
        timer = stoptime-starttime
        return liczby, timer 
    return wrapper

# sortowanie bąbelkowe
@measuretime
def buble_sort(liczby):
    for i in range(len(liczby)):
        for j in range(len(liczby)-1):
            if liczby[j]>liczby[j+1]:
                liczby[j], liczby[j+1] = liczby[j+1], liczby[j] #flip flop by Python
    return liczby
    
# sortowanie przez wstawianie
@measuretime
def insert_sort(liczby):
    for i in range(1,len(liczby)):
        key = liczby[i]
        j=i-1
        while j>= 0 and liczby[j] > key:
            liczby[j+1] = liczby[j]
            j-=1
        liczby[j+1] = key
    return liczby

# sortowanie przez wybór
@measuretime
def selection_sort(liczby):
    for i in range(len(liczby)):
        smallest_element = min(liczby[i:])
        index_of_smallest = liczby.index(smallest_element)
        liczby[i], liczby[index_of_smallest] = liczby[index_of_smallest], liczby[i]
    return liczby

# sortowanie szybkie
@measuretime
def quick(liczby):
    nums = quicksort(liczby)
    return nums
        
def quicksort(liczby):
    if len(liczby) <= 1:
        return liczby 
    pivot = liczby[len(liczby) // 2] 
    left = [x for x in liczby if x < pivot] 
    middle = [x for x in liczby if x == pivot] 
    right = [x for x in liczby if x > pivot]  

    return quicksort(left) + middle + quicksort(right)

# wyświetlanie liczb
def show_nums(nums, when=True, timer=0):
    if when == True and timer == 0:
        print("\nLiczby przed sortowaniem: \n")
        print(nums)
    else:
        print("\nLiczby po posortowaniu: \n")
        print(nums)
        print(f"\n===== Czas sortowania: {timer}s. =========")
    
    
# main
def main_f():
    czygen = True
    while True:
        if czygen == True:
            d = int(input("Podaj dolny zakres liczb: "))
            g = int(input("Podaj górny zakres liczb: "))
            if d > g:
                d, g = g, d
            ile = int(input("Ile liczb chcesz mieć w liście? "))
            print("\n")
            liczby_g = [rdi(d,g) for i in range(0,ile) ]
        
        
        print("="*30)
        menu()
        print("="*30)
        wybor = input("Jaka metoda sortowania? ")
        
        if wybor in ('b', 'i', 's', 'q'):
            posort=[]
            
            if wybor == 'b':
                liczby_1 = liczby_g.copy()  
                show_nums(liczby_1, True)
                posort, timer = buble_sort(liczby_1)
                show_nums(posort, False, timer)
            elif wybor == 'i':
                liczby_1 = liczby_g.copy()  
                show_nums(liczby_1, True)
                posort, timer = insert_sort(liczby_1)
                show_nums(posort, False, timer)
            elif wybor == 's':
                liczby_1 = liczby_g.copy()  
                show_nums(liczby_1, True)
                posort, timer = selection_sort(liczby_1)
                show_nums(posort, False, timer)
            elif wybor == 'q':
                liczby_1 = liczby_g.copy()  
                show_nums(liczby_1, True)
                posort, timer = quick(liczby_1)
                show_nums(posort, False, timer)
                
            koniec = input("\n Czy chcesz kontynuować? t/n ")
            if koniec != 't':
                break
            else:
                wyb = input("\n Czy chcesz wygenerować nowe liczby? t/n ")
                if wyb in ('t','n'):
                    if wyb == 't':
                        czygen = True
                    else:
                        czygen = False
                else:
                    print("Wybierz poprawnie... ")
        else:
            print("Zły wybór łosiu!")
    print("\nDziękujemy za współpracę :P \n")
      
# =========== MAIN ========================  
main_f()             