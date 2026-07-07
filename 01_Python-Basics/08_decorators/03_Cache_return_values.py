# Implement a decorator that caches the return values of a fn, so that when it is called with 
    # the same arguments the cached value is returned instead of reexecuting the fn...

import time

def cache(func):
    cache_value = {}
   # print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result        
    return wrapper

@cache
def long_runnning_function(a,b):
    time.sleep(4)
    return a+b

print(long_runnning_function(2,3))
print(long_runnning_function(5,3))
print(long_runnning_function(6,3))
print(long_runnning_function(7,3))
print(long_runnning_function(8,3))
print(long_runnning_function(5,3))
print(long_runnning_function(2,3))
