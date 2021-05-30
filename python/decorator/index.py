from time import perf_counter
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        arg = str(*args)
        print(f'Duration {duration: .8f}s of {result} {arg}')
        return result
    return wrapper

@timer
def fib(n): 
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(8))

# def fib(a,b,c):
#     def get_three():
#         return (a,b,c)
    
#     return get_three

# my_foo = fib(1,2,3)
# print(my_foo())