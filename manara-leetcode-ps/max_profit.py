# Understand 
#   - Input > prices = [1, 3, 7, 2, 4]
#   - Output > return the diff that have max profit
#   - Constraints > you must buy before you sell.

# My example Input: prices = [7,1,5,3,6,4]
#   Output: 5
#   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#   Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Brute Force Soultion
# def maxProfit( prices) -> int:
#         max = 0
#         buy, sell = 1, 1
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[j] - prices[i] > max:
#                     max = prices[j] - prices[i] 
#         return max

# Find the BottlenFeck (Problem) 
    # The Problem in nested loop it is cost O(n^2)

# Optimize Best DS or Pattern  {One Pass}
# Implement code

def maxProfit(prices): # prices = [7,1,5,3,6,4]
    min_price = prices[0]
    max_profit = 0 
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit

# Test & Complexity { Tine O(n), Space O(1) }

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))

