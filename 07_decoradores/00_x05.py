# slow down
import functools
import time

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down



@slow_down
def funcion_lenta():
    "ejectuar despacio"
    
    print("ejecutada")
    pass

def funcion_normal():
    "ejecutar rapido"
    
    print("ejecutada")
    pass

funcion_normal()

funcion_lenta()