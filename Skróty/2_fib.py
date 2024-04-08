'''
Skrót przydatny na maturę
#2 - jednolinijkowy ciąg fibonacciego
Jakub Rutkowski 2024
'''

def fib(n):
    return fib(n-1)+fib(n-2) if n>1 else n

print(fib(10)) # 55