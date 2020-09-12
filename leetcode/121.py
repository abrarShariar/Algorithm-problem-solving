class Solution:
		def maxProfit(self, prices) -> int:
			if len(prices) == 0:
				return 0
			# buy => lowest
			# sell => highest
			buy_price = prices[0]
			max_profit = 0

			for i in range(1, len(prices)):
				current_price = prices[i]
				if current_price < buy_price:
					buy_price = current_price
					continue
				else:
					max_profit = max(max_profit, current_price - buy_price)

			return max_profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit([2,4,1]))
