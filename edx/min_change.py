# SOLVed
def dp_changer(m):
    coins = [1,3,4]
    # matrix to keep track of all the min changges
    min_changes = {}
    # set the initial to 0
    min_changes[0] = 0
    # start taking into consideration all the money [1..money]
    for current_money in range(1, m + 1):
        # set min changes to inifity first
        min_change_amount = float('inf')
        # start with all the coins
        for coin in coins:
            if coin <= current_money:
                rem_amount = current_money - coin
                # the number of coins is the minimum changes of the remaining amount + the coin
                num_of_coins = min_changes[rem_amount] + 1
                min_change_amount = min(num_of_coins, min_change_amount)

        min_changes[current_money] = min_change_amount

    return min_changes[m]

print(dp_changer(2, [1,3,4]))
print(dp_changer(34, [1,3,4]))