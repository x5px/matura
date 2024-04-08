import time

def pomiar_czasu(func, *kwargs):
    def wrapper(*kwargs):
        start_time = time.time()
        func(*kwargs)
        print(time.time() - start_time)
    return wrapper
