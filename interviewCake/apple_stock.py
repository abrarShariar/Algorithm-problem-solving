def greedy(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError("Stock prices index out of range")

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for i in range(1,len(stock_prices)):
        current_price = stock_prices[i]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(current_price, min_price)

    return max_profit

def main():
    arr = [10, 7, 5, 4, 2, 1]
    print(greedy(arr))

main()
