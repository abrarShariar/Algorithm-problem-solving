def div(x):
    x += 1
    while (x%10 == 0):
        x //= 10

    return x

def main():
    a = set()
    n = int(input())

    while (not (n in a)):
        a.add(n)
        n = div(n)

    print(len(a))

if __name__ == "__main__":
    main()
