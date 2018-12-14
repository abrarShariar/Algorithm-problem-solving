

def primeCount(n):
    sieve = [x+2 for x in range(n-1)]
    for i in range(int(n/2)):
        num = i + 2
        index = 2
        nextStep = num * index
        while nextStep <= n:
            if nextStep in sieve:
                sieve.remove(nextStep)
            index += 1
            nextStep = num * index

    print(sieve)
    return len(sieve)


# q = int(input())

print(primeCount(30))
