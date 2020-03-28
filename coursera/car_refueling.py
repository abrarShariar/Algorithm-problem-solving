input_arr = [0, 200, 375, 550, 750, 950]
numRefill = 0
currentRefill = 0
limit = 400
n = len(input_arr) - 2
# print(n)

while (currentRefill <= n):
    lastRefill = currentRefill
    while (currentRefill <= n and input_arr[currentRefill+1] - input_arr[lastRefill] <= limit):
        currentRefill += 1

    if currentRefill == lastRefill:
        print("IMPOSSIBLE")
        break

    if currentRefill <= n:
        numRefill += 1

print(numRefill)
