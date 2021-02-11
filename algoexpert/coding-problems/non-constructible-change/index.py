def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    max_coin = coins[len(coins) - 1]
    # count the max till max_coin
    second_greatest_possible = 0
    
    for i in range(len(coins) - 1):
        second_greatest_possible += coins[i]
    
    # prepare a dictionary
    coin_count_dict = {}
    for i in range(1, max_coin):
        coin_count_dict[coins[i]] = coin_count_dict.get(coins[i], 0) + 1

    # start from the second greatest possible
    # go to previous
    # check if 




