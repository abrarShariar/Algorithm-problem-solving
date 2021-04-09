
# SOLVED!
number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    # get the number of houses and total money
    number_of_houses, total_money = list(map(int, input().split(' ')))
    house_costs = list(map(int, input().split(' ')))
    house_costs.sort()
    house_count = 0
    for cost in house_costs:
        if cost > total_money:
            break
        else:
            total_money -= cost
            house_count += 1

    print("Case #{}: {}".format(i, house_count))

