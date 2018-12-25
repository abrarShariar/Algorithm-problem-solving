def greedy(arr):
    if len(arr) < 2:
        raise ValueError("Stock prices index out of range")
        
    min_price = arr[0]
    max_profit = arr[1] - arr[0]

    for current_price in arr:
        min_price = min(current_price, min_price)
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)

    return max_profit

def main():
    arr = [10, 7, 5, 4, 2, 1]
    print(greedy(arr))

main()
