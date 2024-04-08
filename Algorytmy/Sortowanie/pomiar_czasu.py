"""
Pomiar czasu wykonania funkcji
"""
import time

def mierzenie_czasu(func, *kwargs):
    def wraper(*kwargs):
        start_time = time.perf_counter()
        wynik = func(*kwargs)
        stop_time = time.perf_counter()
        print(f"Funkcja działała przez {stop_time-start_time} s.")
        return wynik
    return wraper
        
        