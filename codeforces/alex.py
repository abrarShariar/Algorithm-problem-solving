def main():
    n = int(input())
    if n == 1:
        return 1

    cell = 1
    gap = 4

    for i in range(2, n+1):
        cell = cell + gap
        gap = gap + 4

    return cell


if __name__ == '__main__':
    res = main()
    print(res)
