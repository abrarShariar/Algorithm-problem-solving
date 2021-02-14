def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()

    if len(coins) == 0:
        return 1
    elif len(coins) == 1:
        return 2 if coins[0] == 1 else 1
    
    running_sum = coins[0]
    for i in range(1, len(coins)):
        current_coin = coins[i]
        if not (current_coin <= running_sum) and current_coin != running_sum + 1:
            return running_sum + 1

        running_sum += current_coin
    
    return running_sum + 1

print(nonConstructibleChange([1,2,4]))
print(nonConstructibleChange([1]))
print(nonConstructibleChange([0]))

print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))

print(nonConstructibleChange([1, 5, 1, 1, 1, 10, 15, 20, 100]))





