# Uses python3
import sys

# SOLVED
def optimal_summands(n):
    summands = []
    running_n = n
    for i in range(1,n+1):
        # in buffer now
        remaining = running_n - i
        if remaining > i:
            summands.append(i)
            running_n = running_n - i
        else:
            summands.append(running_n)
            break

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
