fib_dict = {}
fib_dict[0] = 0
fib_dict[1] = 1

def fibo(n):
    if n == 1 or n == 0:
        return fib_dict[n]

    if n in fib_dict:
        return fib_dict[n]
    
    fib_dict[n] = fibo(n-1) + fibo(n-2)
    return fib_dict[n]
 
print(fibo(3))