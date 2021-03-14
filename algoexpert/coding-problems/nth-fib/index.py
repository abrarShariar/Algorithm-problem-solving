def getNthFib(n):
    if n == 1 or n == 2:
        return n

    return getNthFib(n-1) + getNthFib(n-2)

print(getNthFib(3))