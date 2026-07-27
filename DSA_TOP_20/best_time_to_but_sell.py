'''
def maxProfit(prices):
    n = len(prices)
    maximum_profit = 0

    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            maximum_profit = max(maximum_profit, profit)

    return maximum_profit


# Input
prices = list(map(int, input("Enter stock prices: ").split()))

# Output
print("Maximum Profit:", maxProfit(prices))
'''
# ----------------------------
'''
min_price = min(min_price, price)

profit = price - min_price

max_profit = max(max_profit, profit)
'''

def max_profite_price(prices):
    min_price = float("inf") # ∞
    max_profite = 0
    
    for price in prices:
        min_price = min(min_price, price)
        profite = price - min_price
        max_profite = max(max_profite, profite)
    
    return max_profite    

prices = list(map(int, input("Enter stock prices: ").split()))
print("Maximum Profit: ", max_profite_price(prices))