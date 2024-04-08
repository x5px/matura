'''
Quick Sort
K>K> 2023
'''
def quick_sort(liczby):
    if len(liczby) <= 1:
        return liczby 
    pivot = liczby[len(liczby) // 2] 
    left = [x for x in liczby if x < pivot] 
    middle = [x for x in liczby if x == pivot] 
    right = [x for x in liczby if x > pivot]  

    return quick_sort(left) + middle + quick_sort(right)

liczby = [2, 5, 1, 8, 4, 0, 9]
print(f"Liczby przed sortowaniem: {liczby}")
liczby = quick_sort(liczby)  
print(f"Liczby przed sortowaniem: {liczby}")