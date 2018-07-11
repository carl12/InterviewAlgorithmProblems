#  Write an efficient function that takes stock_prices and returns the best profit I could have made from one purchase and one sale of one share of Apple stock yesterday.
# For example:
#   stock_prices = [10, 7, 5, 8, 11, 9]
# get_max_profit(stock_prices)
# # Returns 6 (buying for $5 and selling for $11)

# No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass. 

def find_best_trade(prices):
	if len(prices) < 2:
		raise ValueError('Stock price list must have more than 1 price')

	#initialize max and min using first two stock prices
	min_price = min(prices[0], prices[1])
	max_diff = prices[1] - prices[0]

	# Check for greater difference and then a new min for each price
	for c in costs[2:]:
		max_diff = max(max_diff, c - min_price)
		min_price = min(c, min_price)

	return diff

print(find_best_trate([6,2,1,0.1]))
print(find_best_trate([5,1,4,6,0]))
print(find_best_trate([0,0,0,0]))
print(find_best_trate([100,5,1,1,30]))
print(find_best_trate([1,2,1,3,4,2,6]))
# print(sys.maxsize)

